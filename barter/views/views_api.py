from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Item, BarterLog
from ..utils.serialisers import ItemSerializer
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user.models import CustomUser
from ..utils.serialisers import ItemSerializer
from ..utils.authenticators import CookieJWTAuthentication

class ItemListAPIView(APIView):
    def get(self, request):
        query_set = BarterLog.objects.filter(
            buyer_request_time__isnull=True
        )
        item_list = {}

        for instance in query_set:
            serializer = ItemSerializer(instance.item)
            item_list[instance.item.itemId] = serializer.data

        return Response({
            "item_list": item_list,
        })
    
class SearchItemAPIView(APIView):
    def post(self, request):
        search_query = request.data['search']
        query_set = Item.objects.filter(Q(name__icontains=search_query) | Q(description__icontains=search_query))

        print(query_set)

        search_result = {}

        for i in query_set:
            serializer = ItemSerializer(i)
            search_result[i.itemId] = serializer.data

        return Response({
          "search_result": search_result
        })
    
class CreateItemAPIView(APIView):

    authentication_classes = [CookieJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ItemSerializer(data=request.data)

        print(request.user)
        print('hi')

        if serializer.is_valid():
            serializer.save(seller=request.user)
            return Response(
                {"message": "Item created successfully"},
                status=201
            )

        return Response(serializer.errors, status=400)