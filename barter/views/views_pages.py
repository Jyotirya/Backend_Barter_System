from django.shortcuts import render

def barterView(request):
    return render(request, 'barter_temp/barter_details.html', {})