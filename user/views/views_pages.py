from django.shortcuts import render

def UserPageView(request):
    return render(request, 'user_temp/user_details.html', {})

def LoginPageView(request):
    return render(request, 'user_temp/login.html', {})

def RegisterPageView(request):
    return render(request, 'user_temp/register.html', {})

def LogoutPageView(request):
    return render(request, 'user_temp/logout.html', {})