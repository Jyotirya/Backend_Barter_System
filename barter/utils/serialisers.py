# barter/serializers.py
from rest_framework import serializers
from ..models import Item, ItemImage

class ItemSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = [
            "itemId",
            "name",
            "price",
            "description",
            "deadline",
            "status",
            "condition",
            "tags",
            "images"
        ]

    def get_status(self, obj):
        return obj.barter_status()
    
    def get_images(self, obj):
        return [img.image_url for img in obj.image_set.all()]
    
class ItemImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemImage
        fields = ["image_url"]