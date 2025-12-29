from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'properties', PropertyViewSet)
router.register(r'zones', ZoneViewSet)
router.register(r'buildings', BuildingViewSet)
router.register(r'floors', FloorViewSet)
router.register(r'exposures', ExposureViewSet)
router.register(r'attributes', AttributeViewSet)
router.register(r'bed-types', BedTypeViewSet)
router.register(r'room-types', RoomTypeViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'add-on-items', AddOnItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]