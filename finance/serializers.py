from rest_framework import serializers
from .models import *

class MarketSegmentSerializer(serializers.Serializer):
    class Meta:
        model = MarketSegment
        fields = '__all__'

class RatePlanSerializer(serializers.Serializer):
    class Meta:
        model = RatePlan
        fields = '__all__'

class RoomRateSerializer(serializers.Serializer):
    class Meta:
        model = RoomRate
        fields = '__all__'