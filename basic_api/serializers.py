from basic_api.models import DRFPost
from rest_framework import serializers


class DRFPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = DRFPost
        fields = '__all__'
