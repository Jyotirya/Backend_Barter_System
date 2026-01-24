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
    )


app_name = 'barter_api'
urlpatterns = [
    path('items/', ItemListAPIView.as_view()),
    path('search/', SearchItemAPIView.as_view()),
    path('create/', CreateItemAPIView.as_view()),
    path('delete/<str:itemId>/', DeleteItemAPIView.as_view()),
    path('request/<str:itemId>/', RequestItemAPIView.as_view()),
    path('accept/<str:itemId>/', AcceptItemAPIView.as_view()),
    path('pending-requests/', DisplayRequestedItemAPIView.as_view()),
    path('add/<str:itemId>/', AddToWishListAPIView.as_view()),
]