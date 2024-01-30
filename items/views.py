from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item

# all item route func
def home(request):
    allItem = Item.objects.all()
    return render(request, 'items/index.html', {'allItem': allItem})

# add item route func
def addItem(request):
    
    newItem = request.POST['item']

    if newItem == "":
        return redirect('/')
    
    else:

        itemObj = Item()
        itemObj.item = newItem
        itemObj.save()
        return redirect("/")


# delete item route func
def delItem(request, id):

    all = Item.objects.all()
    
    for itemObj in all:
        if(itemObj.id == id):
            itemObj.delete()
            return redirect("/")
            break
    else:
        return redirect("/")


# not found route func
def error404(request, exception):
    return render(request, '404.html')