from django.urls import path, include
from ..views.views_pages import RegisterPageView, LoginPageView, UserPageView, LogoutPageView

app_name = 'user_pages'
urlpatterns = [
    path('signup/', RegisterPageView, name='register'),
    path('login/', LoginPageView, name='register'),
    path('me/', UserPageView, name='register'),
    path('logout/', LogoutPageView, name='register'),
]