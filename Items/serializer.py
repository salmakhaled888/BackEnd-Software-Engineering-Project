from Items.models import Item
from rest_framework import serializers

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['itemName', 'description', 'barcode_id', 'price', 'photo', 'inStock']