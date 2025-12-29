from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'market-segments', MarketSegmentViewSet)
router.register(r'rate-plans', RatePlanViewSet)
router.register(r'room-rates', RoomRateViewSet)
urlpatterns = [
    path('', include(router.urls)),
]