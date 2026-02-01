from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Item, BarterLog, Wishlist
from ..utils.serialisers import ItemSerializer
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from user.serializers import UserSerializer
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

class GetRequestedItemsAPIView(APIView):
    authentication_classes = [CookieJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        query_set = BarterLog.objects.filter(
            buyer_request_time__isnull = False
        )
        
        item_list = {}

        for instance in query_set:
            if instance.item.seller == request.user and instance.seller_accepted_time == None:
                serializer = ItemSerializer(instance.item)
                item_list[instance.item.itemId] = serializer.data

        return Response(item_list)

class GetBuyerAPIView(APIView):
    def post(self, request, *args, **kwargs):

        barter_log = BarterLog.objects.get(item = Item.objects.get(itemId = self.kwargs['itemId']))
        buyer = UserSerializer(barter_log.buyer)
        
        return Response(buyer.data)

        # item = Item.objects.get(itemId = self.kwargs['itemId'])
        
        # seller = UserSerializer(item.seller)

        # return Response(seller.data)
    

class AcceptItemAPIView(APIView):
    authentication_classes = [CookieJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        barter = BarterLog.objects.filter(
            item = Item.objects.filter(itemId=self.kwargs['itemId']).first(),
            buyer_request_time__isnull = False
        )

        if self.kwargs['dec'] == 'accept': 
            barter.update(seller_accepted_time = timezone.now())
            message = 'Accepted Item'
        elif self.kwargs['dec'] == 'decline':
            barter.update(buyer_request_time = None, buyer = '')
            message = 'Declined Item'
        else:
            message = 'Failed to accept/decline, please try again!'

        return Response({
            "message": message
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
            if instance.buyer == request.user:
                serialiser = ItemSerializer(instance.item)
                item_list[instance.item.itemId] = serialiser.data

        return Response(item_list)
    
class AddToWishListAPIView(APIView):
    authentication_classes = [CookieJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        added_item = Item.objects.get(itemId=self.kwargs['itemId'])

        print(added_item)
        
        # for instance in added_item:
        serialiser = ItemSerializer(added_item)


        data = serialiser.data

        wishlist = Wishlist.objects.get(user=request.user)
        item_list = wishlist.item_list

        item_list[self.kwargs['itemId']] = data

        wishlist.item_list = item_list
        wishlist.save()

        return Response({
            "message": "Added to Wishlist"
        })
    
class getWishlistAPIView(APIView):
    authentication_classes = [CookieJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        query_set = Wishlist.objects.get(user = request.user)

        return Response(query_set.item_list)