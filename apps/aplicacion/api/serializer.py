from rest_framework import serializers
from ..models import Cars

class CarsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cars
        fields = '__all__'
    
    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'name': instance['name'],
            'price': instance['price'],
        }
