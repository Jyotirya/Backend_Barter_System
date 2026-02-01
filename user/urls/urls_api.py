from django.urls import path, include
from ..views.views_api import RegisterAPIView, LoginAPIView, UserAPIView, LogoutAPIView

app_name = 'user_ap'
urlpatterns = [
    path('signup/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('me/', UserAPIView.as_view(), name='user'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
]