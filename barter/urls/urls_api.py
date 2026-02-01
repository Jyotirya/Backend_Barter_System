from django.urls import path, include
from ..views.views_api import (
    ItemListAPIView,
    SearchItemAPIView,
    CreateItemAPIView,
    DeleteItemAPIView,
    RequestItemAPIView,
    AcceptItemAPIView,
    DisplayRequestedItemAPIView,
    AddToWishListAPIView,
    GetRequestedItemsAPIView,
    getWishlistAPIView,
    GetBuyerAPIView
    )


app_name = 'barter_api'
urlpatterns = [
    path('items/', ItemListAPIView.as_view()),
    path('search/', SearchItemAPIView.as_view()),
    path('create/', CreateItemAPIView.as_view()),
    path('delete/<str:itemId>/', DeleteItemAPIView.as_view()),
    path('request/<str:itemId>/', RequestItemAPIView.as_view()), # Request Item - Done
    path('requests/', GetRequestedItemsAPIView.as_view()), # Get All Your Items that have been requested - Done
    path('requests/<dec>/<str:itemId>/', AcceptItemAPIView.as_view ()), # Accept/Decline Requested Item - Done
    path('pending-requests/', DisplayRequestedItemAPIView.as_view()), # Display Items that you have requested - Done
    path('add/<str:itemId>/', AddToWishListAPIView.as_view()),
    path('wishlist/', getWishlistAPIView.as_view()),
    path('buyer/<itemId>/', GetBuyerAPIView.as_view()),
]