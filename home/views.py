from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import order

# Create your views here.
def index(request):
    if request.method =="POST":
        iteam = request.POST.get('iteam')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        Orders = order(iteam=iteam, price=price, quantity=quantity, date=datetime.today())
        Orders.save()
    return render(request,'index.html')
