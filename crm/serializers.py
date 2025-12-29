from rest_framework import serializers
from .models import *

class GenderSerializer(serializers.Serializer):
     class Meta:
        model = Gender
        fields = '__all__'

class CountrySerializer(serializers.Serializer):
     class Meta:
        model = Country
        fields = '__all__'

class GuestSerializer(serializers.Serializer):
        country = CountrySerializer(read_only=True)
        class Meta:
            model = Guest
            fields = [
                 'id','gender','name','profile','is_owner','is_vip','owner_name',
                 'address','country','state','city','zip_code',
                 'mobile_code','mobile_no','tele_code','tele_no',
                 'email','identity_type','nationality',
                 'id_card', 'passport_number', 'local_name',
                 'date_of_birth', 'issue_date', 'expire_date', 'is_primary'
            ]

class OrganizationSerializer(serializers.Serializer):
     class Meta:
        model = Organization
        fields = '__all__'
    
class ARAccountSerializer(serializers.Serializer):
     class Meta:
        model = ARAccount
        fields = '__all__'  