from django.shortcuts import render

def ItemListPageView(request):
    return render(request, 'barter_temp/list_items.html', {})

def SearchItemPageView(request):
    return render(request, 'barter_temp/search.html', {})

def CreateItemPageView(request):
    return render(request, 'barter_temp/create.html', {})

def AcceptItemPageView(request):
    return render(request, 'barter_temp/accept.html', {})

def AddToWishListPageView(request):
    return render(request, 'barter_temp/wishlist.html', {})
