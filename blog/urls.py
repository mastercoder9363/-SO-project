from django.contrib import admin
from django.urls import path
from core.views import *
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', index),
    path('home/', index, name="home"),
    path('fast/', fast, name="fast"),
    path('milliy/', milliy, name="milliy"),
    path('shirin/', shirin, name="shirin"),
    path('ichimlik/', ichimlik, name="ichimlik"),
    path('', views.LoginView.as_view(template_name='index1.html'))
]
