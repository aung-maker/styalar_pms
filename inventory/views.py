from rest_framework import viewsets
from .models import *
from .serializers import *
from root.permissions import IsAdminOrReadOnly


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAdminOrReadOnly]

class ZoneViewSet(viewsets.ModelViewSet):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer
    permission_classes = [IsAdminOrReadOnly]


class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    permission_classes = [IsAdminOrReadOnly]

class FloorViewSet(viewsets.ModelViewSet):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer
    permission_classes = [IsAdminOrReadOnly]

class ExposureViewSet(viewsets.ModelViewSet):
    queryset = Exposure.objects.all()
    serializer_class = ExposureSerializer
    permission_classes = [IsAdminOrReadOnly]

class AttributeViewSet(viewsets.ModelViewSet):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer
    permission_classes = [IsAdminOrReadOnly]

class BedTypeViewSet(viewsets.ModelViewSet):
    queryset = BedType.objects.all()
    serializer_class = BedTypeSerializer
    permission_classes = [IsAdminOrReadOnly]

class RoomTypeViewSet(viewsets.ModelViewSet):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer
    permission_classes = [IsAdminOrReadOnly]

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAdminOrReadOnly]

    # TODO: Filter: I need to add more filters later
    def get_queryset(self):
        queryset = Room.objects.all()
        status = self.request.query_params.get('status')
        if status:
            queryset = queryset.filter(maid_status=status)
        return queryset

class RoomTypeViewSet(viewsets.ModelViewSet):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer
    permission_classes = [IsAdminOrReadOnly]

class AddOnItemViewSet(viewsets.ModelViewSet):
    queryset = AddOnItem.objects.all()
    serializer_class = AddOnItemSerializer
    permission_classes = [IsAdminOrReadOnly]