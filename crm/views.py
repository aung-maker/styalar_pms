from rest_framework import viewsets
from .models import *
from .serializers import *
from root.permissions import IsAdminOrReadOnly

class GenderViewSet(viewsets.ModelViewSet):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer
    permission_classes = [IsAdminOrReadOnly]

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAdminOrReadOnly]
    
class GuestViewSet(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    permission_classes = [IsAdminOrReadOnly]

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAdminOrReadOnly]

class ARAccountViewSet(viewsets.ModelViewSet):
    queryset = ARAccount.objects.all()
    serializer_class = ARAccountSerializer
    permission_classes = [IsAdminOrReadOnly]