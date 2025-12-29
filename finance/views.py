from rest_framework import viewsets
from .models import *
from .serializers import *
from root.permissions import IsAdminOrReadOnly

class MarketSegmentViewSet(viewsets.ModelViewSet):
    queryset = MarketSegment.objects.all()
    serializer_class = MarketSegmentSerializer
    permission_classes = [IsAdminOrReadOnly]

class RatePlanViewSet(viewsets.ModelViewSet):
    queryset = RatePlan.objects.all()
    serializer_class = RatePlanSerializer
    permission_classes = [IsAdminOrReadOnly]

class RoomRateViewSet(viewsets.ModelViewSet):
    queryset = RoomRate.objects.all()
    serializer_class = RoomRateSerializer   
    permission_classes = [IsAdminOrReadOnly]