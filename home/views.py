from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import order

# Create your views here.
def index(request):
    if request.method =="POST":
        if request.POST.get('iteam'):
            savevalue=order()
            # savevalue.iteam=request.POST.get('iteam')
            # savevalue.save()
        iteam = request.POST.get('iteam')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        Orders = order(iteam=iteam, price=price, quantity=quantity,email=email, desc=desc, date=datetime.today())
        Orders.save()
    return render(request,'index.html')
