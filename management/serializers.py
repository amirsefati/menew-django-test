from rest_framework import serializers
from .models import Equipment


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ['id', 'name', 'price',
                  'flag', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
