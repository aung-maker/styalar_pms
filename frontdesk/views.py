from rest_framework import viewsets
from .models import *
from .serializers import *
from root.permissions import IsAdminOrReadOnly


class SourceViewSet(viewsets.ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    permission_classes = [IsAdminOrReadOnly]

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAdminOrReadOnly]