from rest_framework import serializers
from .models import Silabo

class SilaboSerializer(serializers.ModelSerializer):
    class Meta:
        model = Silabo
        fields = '__all__'
