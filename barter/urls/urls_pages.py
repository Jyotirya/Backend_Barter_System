from django.urls import path, include
from ..views.views_pages import ItemListPageView

app_name = 'barter_pages'
urlpatterns = [
    path('', ItemListPageView, name='barter')
]