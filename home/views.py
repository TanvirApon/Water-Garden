from django.shortcuts import render,HttpResponse
from .models import Fish,Product,Food,Orders
from math import ceil

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def fishes(request):
    Fishs = Fish.objects.all()
    print(Fishs)
    n = len(Fishs)
    nSlides = n//4 + ceil ((n/4)-(n//4))         
    params={'no_of_slides':nSlides,'range':(1,nSlides),'Fish':Fishs}
    return render(request,'fishes.html',params)

def contact(request):
    return render(request,'contact.html')

def aqurium(request):
    Products = Product.objects.all()
    print(Products)
    n = len(Products)
    nSlides = n//4 + ceil ((n/4)-(n//4))         
    params={'no_of_slides':nSlides,'range':(1,nSlides),'Product':Products}
    return render(request,'aqurium.html',params)

def food(request):
    Foods = Food.objects.all()
    print(Foods)
    n = len(Foods)
    nSlides = n//4 + ceil ((n/4)-(n//4))         
    params={'no_of_slides':nSlides,'range':(1,nSlides),'Food':Foods}
    return render(request,'food.html',params)

def order(request):
    if request.method=="POST":
        items_json= request.POST.get('itemsJson', '')
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        address=request.POST.get('address', '') 
        city=request.POST.get('city', '')
        phone=request.POST.get('phone', '')

        order = Orders(items_json= items_json, name=name, email=email, address= address, city=city, phone=phone)
        order.save()
        thank=True
        id=order.order_id
        return render(request, 'checkout.html/', {'thank':thank, 'id':id})
    return render(request,'checkout.html')

def product(request,myid):
          product = Product.objects.filter(id=myid)
          return render(request,'product.html', {'product':product[0]})    

def fishview(request,myid):
        fish = Fish.objects.filter(id=myid)
        return render(request,'fishview.html',{'fishview':fish[0]})

def foodview(request,myid):
        food = Food.objects.filter(id=myid)
        return render(request,'foodview.html',{'foodview':food[0]})    

