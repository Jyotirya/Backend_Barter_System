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

    # def create(self, validated_data):
    #     name = validated_data.pop('name', None)
    #     price = validated_data.pop('price', None)
    #     deadline = validated_data.pop('deadline', None)

    #     instance = self.Meta.model(**validated_data)

    #     if name is not None and price is not None and deadline is not None:
    #         instance.save()

    #     return instance