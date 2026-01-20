from django.urls import path, include
from ..views.views_pages import barterView

app_name = 'barter_pages'
urlpatterns = [
    path('', barterView, name='barter')
]