from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Item, BarterLog, Wishlist
from ..utils.serialisers import ItemSerializer
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from user.models import CustomUser
from ..utils.serialisers import ItemSerializer
from ..utils.authenticators import CookieJWTAuthentication
from django.utils import timezone

class ItemListAPIView(APIView):
    authentication_classes = [CookieJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        query_set = BarterLog.objects.filter(
            buyer_request_time__isnull=True,
        )
        item_list = {}

        for instance in query_set:
            if instance.item.seller != request.user:
                serializer = ItemSerializer(instance.item)
                item_list[instance.item.itemId] = serializer.data

        return Response(item_list)
    
class SearchItemAPIView(APIView):
    def post(self, request):
        search_query = request.data['search']
        query_set = Item.objects.filter(
            Q(name__icontains=search_query) | 
            Q(description__icontains=search_query)
        )

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

        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
            
        created_item = serializer.save(seller=request.user)

        BarterLog.objects.create(
            item = created_item,
        )

        return Response(
            {"message": "Item created successfully"},
            status=201
        )
    
# class UpdateItemAPIView(APIView):
#     authentication_classes = [CookieJWTAuthentication]
#     permission_classes = [IsAuthenticated]

#     def post(self, request, *args, **kwargs):
#         item = Item.objects.filter(itemId = self.kwargs['itemId'])

#         serializer = ItemSerializer(data = request.data)

#         if not serializer.is_valid():
#             return Response(serializer.errors, status=400)
            
#         created_item = serializer.save(seller=request.user)
    
class DeleteItemAPIView(APIView):
    authentication_classes = [CookieJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        item = Item.objects.filter(
            itemId = self.kwargs['itemId']
        )

        item.delete()

        if Item.objects.filter(itemId = self.kwargs['itemId']).exists():
            return Response({
                "message": "Error in deleting item"
            })
        
        return Response({
            "message": "Item deleted successfully"
        })
    
class RequestItemAPIView(APIView):

    authentication_classes = [CookieJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        barter = BarterLog.objects.filter(item = (Item.objects.filter(itemId=self.kwargs['itemId']).first()))

        barter.update(buyer_request_time = timezone.now())
        barter.update(buyer = request.user)

        return Response({
            "message": 'Requested'
        })
    
class AcceptItemAPIView(APIView):

    authentication_classes = [CookieJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        barter = BarterLog.objects.filter(
            item = Item.objects.filter(itemId=self.kwargs['itemId']).first(),
            buyer_request_time__isnull = False
        )
        
        barter.update(seller_accepted_time = timezone.now())


        return Response({
            "message": "Accepted Item"
        })
    
class DisplayRequestedItemAPIView(APIView):
    authentication_classes = [CookieJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        query_set = BarterLog.objects.filter(
            buyer_request_time__isnull = False,
            seller_accepted_time__isnull = True
        )

        item_list = {}

        for instance in query_set:
            serialiser = ItemSerializer(instance.item)
            item_list[instance.item.itemId] = serialiser.data

        return Response(item_list)
    
class AddToWishListAPIView(APIView):
    authentication_classes = [CookieJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        added_item = Item.objects.filter(itemId=self.kwargs['itemId'])

        serialiser = ItemSerializer(added_item)

        data = serialiser.data

        wishlist = Wishlist.objects.filter(
            user = request.user
        )

        item_list = wishlist.item_list

        item_list[added_item.itemId] = data

        wishlist.update(
            item_list = item_list
        )

        return Response({
            "message": "Added to Wishlist"
        })