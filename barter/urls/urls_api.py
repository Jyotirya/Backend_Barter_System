from django.urls import path, include
from ..views.views_api import ItemListAPIView, ItemModuleAPIView


app_name = 'barter_api'
urlpatterns = [
    path('items/', ItemListAPIView.as_view()),
    path('module/', ItemModuleAPIView.as_view())
    
]