from django.urls import path, include
from ..views.views_pages import ItemListPageView, SearchItemPageView, CreateItemPageView, AcceptItemPageView

app_name = 'barter_pages'
urlpatterns = [
    path('home/', ItemListPageView, name='home'),
    path('search/', SearchItemPageView, name='search'),
    path('create/', CreateItemPageView, name='create'),
    path('accept/', AcceptItemPageView, name='accept'),
]