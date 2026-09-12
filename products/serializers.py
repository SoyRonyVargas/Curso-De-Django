from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = '__all__'
        fields = [
            'id',
            'name',
            'description',
            'price',
            'active',
            'stock',
            'created_at',
        ]
        read_only_fields = [
            'id',
            'created_at',
        ]
        
    def validate_price(self, value):
        print(value)
        if value <= 0:
            raise serializers.ValidationError(
                'El precio debe ser mayor a 0.'
            )
        return value
