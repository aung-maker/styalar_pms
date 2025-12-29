from rest_framework import serializers
from .models import Source, Reservation, ReservationRequest
from inventory.serializers import AddOnItemSerializer
from finance.serializers import MarketSegmentSerializer,RatePlanSerializer
from crm.serializers import OrganizationSerializer,GuestSerializer
from inventory.serializers import RoomSerializer, RoomTypeSerializer
from users.serializers import SimpleUserSerializer


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = '__all__'

class ReservationRequestSerializer(serializers.ModelSerializer):
    item =  AddOnItemSerializer(read_only=True)
    class Meta:
        model = ReservationRequest
        fields = [
           'id','item','unit_price', 'quantity', 
            'date_range_start', 'date_range_end', 'posting_schedule', 
            'folio_target', 'include_in_package', 'total_amount'
        ]


class ReservationSerializer(serializers.ModelSerializer):
    market_segment = MarketSegmentSerializer(read_only=True)
    source = SourceSerializer(read_only=True)
    organization = OrganizationSerializer(read_only=True)
    room = RoomSerializer(read_only=True)
    room_type = RoomTypeSerializer(read_only=True)
    rate_plan = RatePlanSerializer(read_only=True)
    guests = GuestSerializer(many=True)
    primary_guest = GuestSerializer(read_only=True)
    requests = ReservationRequestSerializer(many=True, required=False)
    created_by = SimpleUserSerializer(read_only=True)
    updated_by = SimpleUserSerializer(read_only=True)
    

    class Meta:
        model = Reservation
        fields = [
           'id','arrival_date','departure_date','arrival_time','departure_time',
              'adults', 'children','market_segment', 'source', 'organization',
              'room', 'room_type', 'rate_plan', 'total_amount',
              'guests', 'primary_guest', 'reservation_number', 'reservation_type',
              'created_by','updated_by', 'created_at', 'updated_at', 'requests'
        ]
        read_only_fields = ['reservation_number', 'created_by', 'created_at']

    def create(self, validated_data):
        # 1. Pop nested data and M2M fields
        requests_data = validated_data.pop('requests', [])
        guests = validated_data.pop('guests', [])
        special_reqs = validated_data.pop('special_requests', [])
        
        # 2. Inject the authenticated user into the data
        user = self.context['request'].user
        if user and user.is_authenticated:
            validated_data['created_by'] = user

        # 3. Create the Reservation
        reservation = Reservation.objects.create(**validated_data)
        
        # 4. Set Many-to-Many Relationships
        if guests:
            reservation.guests.set(guests)
        if special_reqs:
            reservation.special_requests.set(special_reqs)

        # 5. Create Nested Requests (Add-ons)
        for req_data in requests_data:
            ReservationRequest.objects.create(reservation=reservation, **req_data)

        return reservation

def update(self, instance, validated_data):
        # 1. Extract the authenticated user from the request context
        user = self.context['request'].user
        
        # 2. Extract nested data
        requests_data = validated_data.pop('requests', None)
        guests = validated_data.pop('guests', None)
        special_reqs = validated_data.pop('special_requests', None)

        # 3. Update standard fields AND the audit field
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        if user and user.is_authenticated:
            instance.updated_by = user  # Track who did the update

        # 4. Sync M2M (Guests & Special Requests)
        if guests is not None:
            instance.guests.set(guests)
        if special_reqs is not None:
            instance.special_requests.set(special_reqs)

        instance.save()

        # 5. Smart Sync for Reservation Requests
        if requests_data is not None:
            keep_ids = []
            for item_data in requests_data:
                req_id = item_data.get('id')
                if req_id:
                    # Update existing request
                    req_obj = ReservationRequest.objects.get(id=req_id, reservation=instance)
                    for attr, value in item_data.items():
                        setattr(req_obj, attr, value)
                    req_obj.save()
                    keep_ids.append(req_obj.id)
                else:
                    # Create new request
                    new_req = ReservationRequest.objects.create(reservation=instance, **item_data)
                    keep_ids.append(new_req.id)
            
            # Delete removed items
            instance.requests.exclude(id__in=keep_ids).delete()

        return instance