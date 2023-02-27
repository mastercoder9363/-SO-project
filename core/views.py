from django.shortcuts import render
from .models import FastFood, MilliyTaom, Shirinlik, Ichimlik

def index(request):
    return render(request, 'index.html')

def index(request):
    return render(request, 'index.html')

def fast(request):
    fast=FastFood.objects.all()
    context={
        'fast': fast
    }
    return render(request, 'fast.html', context)

def milliy(request):
    milliy=MilliyTaom.objects.all()
    context={
        'milliy': milliy
    }
    return render(request, 'milliy.html', context)

def shirin(request):
    shirin=Shirinlik.objects.all()
    context={
        'shirin': shirin
    }
    return render(request, 'shirin.html', context)

def ichimlik(request):
    ichimlik=Ichimlik.objects.all()
    context={
        'ichimlik': ichimlik
    }
    return render(request, 'ichimlik.html', context)

def index1(request):
    return render(request, 'index1.html')