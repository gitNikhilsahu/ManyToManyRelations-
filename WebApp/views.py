from django.shortcuts import render
from .models import Driver

def driverlist(request):
    items = Driver.objects.all()
    return render(request, 'CarDriver.html', {'items':items})
