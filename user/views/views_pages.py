from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# @method_decorator(csrf_exempt, name='dispatch')
def UserPageView(request):
    return render(request, 'user_temp/user_details.html', {})

def LoginPageView(request):
    return render(request, 'user_temp/login.html', {})

def RegisterPageView(request):
    return render(request, 'user_temp/register.html', {})

def LogoutPageView(request):
    return render(request, 'user_temp/logout.html', {})