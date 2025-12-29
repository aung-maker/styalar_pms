from rest_framework import serializers
from .models import *

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'

class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = '__all__'

class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'

class FloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Floor
        fields = '__all__'

class ExposureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exposure
        fields = '__all__'

class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = '__all__'

class BedTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BedType
        fields = '__all__'


class RoomTypeBedSerializer(serializers.ModelSerializer):
    bed_details = BedTypeSerializer(source='bed_type', read_only=True)

    class Meta:
        model = RoomTypeBed
        fields = ['quantity', 'bed_details']

class RoomTypeSerializer(serializers.ModelSerializer):
    bed_configuration = RoomTypeBedSerializer(source='roomtypebed_set', many=True, read_only=True)
    attributes = AttributeSerializer(many=True, read_only=True)
    exposures = ExposureSerializer(many=True, read_only=True)
    
    class Meta:
        model = RoomType
        fields = ['id', 'name', 'slug','description','image','max_adult','max_child','max_infant','bed_configuration', 'exposures','attributes', 'base_price']

class RoomSerializer(serializers.ModelSerializer):
    room_type_details = RoomTypeSerializer(source='room_type', read_only=True)
    floor = FloorSerializer(read_only=True)
    class Meta:
        model = Room
        fields = ['id', 'no', 'maid_status', 'room_type','floor', 'room_type_details']

class AddOnItemSerializer(serializers.ModelSerializer):
    available_qty = serializers.SerializerMethodField()

    class Meta:
        model = AddOnItem
        fields = ['id', 'name', 'icon_name', 'default_price', 'total_inventory', 'category', 'available_qty']

    def get_available_qty(self, obj):
        import datetime
        return obj.get_available_qty(datetime.date.today())