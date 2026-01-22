from django.urls import path, include
from ..views.views_api import ItemListAPIView, SearchItemAPIView, CreateItemAPIView


app_name = 'barter_api'
urlpatterns = [
    path('items/', ItemListAPIView.as_view()),
    path('search/', SearchItemAPIView.as_view()),
    path('create/', CreateItemAPIView.as_view()),
]