from rest_framework import serializers
from ..models import *


class transaction_details_serilaizer(serializers.ModelSerializer):
    class Meta:
        model=transaction_details
        fields='__all__'

class transaction_details_update_serilaizer(serializers.ModelSerializer):
    class Meta:
        model=transaction_details
        fields=['details','status']

class r_or_l_serilaizer(serializers.ModelSerializer):
    class Meta:
        model=Register
        fields='__all__'