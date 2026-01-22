from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Item, BarterLog
from ..utils.serialisers import ItemSerializer

class ItemListAPIView(APIView):
    def get(self, request):
        query_set = BarterLog.objects.filter(
            buyer_request_time__isnull=True
        )
        item_list = {}

        for instance in query_set:
            serializer = ItemSerializer(instance.item)
            item_list[instance.item.itemId] = serializer.data

            print(item_list)

        return Response({
            "item_list": item_list,
        })


class ItemModuleAPIView(APIView):
    def get(self, request):
        print(request)
        return Response({
            'test'
        })
