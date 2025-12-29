from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'genders', GenderViewSet)
router.register(r'countries', CountryViewSet)
router.register(r'guests', GuestViewSet)
router.register(r'organizations', OrganizationViewSet)
router.register(r'ar-accounts', ARAccountViewSet)
urlpatterns = [
    path('', include(router.urls)),
]