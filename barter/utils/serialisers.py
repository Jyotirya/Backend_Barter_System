# barter/serializers.py
from rest_framework import serializers
from ..models import Item

class ItemSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = [
            "itemId",
            "name",
            "price",
            "description",
            "deadline",
            "status",
        ]

    def get_status(self, obj):
        return obj.barter_status()