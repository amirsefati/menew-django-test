from rest_framework import serializers
from .models import Estimate, EstimateEquipment

class EstimateEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstimateEquipment
        fields = ['id', 'equipment', 'quantity',
                  'price_override', 'created_on']

class EstimateSerializer(serializers.ModelSerializer):
    equipments = EstimateEquipmentSerializer(many=True, required=False)
    equipments_list = EstimateEquipmentSerializer(source='estimateequipment_set', many=True, required=False)

    class Meta:
        model = Estimate
        fields = ['id', 'note', 'created_on', 'created_by', 'archive', 'equipments', 'equipments_list']

    def create(self, validated_data):
        equipments_data = validated_data.pop('equipments', [])
        estimate = Estimate.objects.create(**validated_data)

        for equipment_data in equipments_data:
            EstimateEquipment.objects.create(estimate=estimate, **equipment_data)

        return estimate

    def update(self, instance, validated_data):
        equipments_data = validated_data.pop('equipments', [])
        
        # Update the Estimate object
        instance.note = validated_data.get('note', instance.note)
        instance.archive = validated_data.get('archive', instance.archive)
        instance.save()

        instance.estimateequipment_set.all().delete()
        for equipment_data in equipments_data:
            EstimateEquipment.objects.create(estimate=instance, **equipment_data)

        return instance
