from rest_framework import serializers
from .models import Item


def validate_price(value):
    if value <= 0:
        raise serializers.ValidationError('Price must be positive')
    return value


class ItemSerializer(serializers.ModelSerializer):
    # Example of field-level validator
    price = serializers.DecimalField(max_digits=10, decimal_places=2, validators=[validate_price])

    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'price', 'created']

    # Object-level validation
    def validate(self, data):
        if 'free' in data.get('name', '').lower() and data.get('price', 0) > 0:
            raise serializers.ValidationError('Items with "free" in the name must have price 0')
        return data
