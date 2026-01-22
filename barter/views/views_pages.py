from django.shortcuts import render

def ItemListPageView(request):
    return render(request, 'barter_temp/list_items.html', {})