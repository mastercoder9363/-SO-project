from django.contrib import admin
from .models import FastFood, MilliyTaom, Shirinlik, Ichimlik

admin.site.register((FastFood, MilliyTaom, Shirinlik, Ichimlik))