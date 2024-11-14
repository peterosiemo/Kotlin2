
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('service/', views.services, name='services'),
    path('starter/', views.starter, name='starter'),
    path('about/', views.about, name='about'),
        path('Doctors/', views.Doctors, name='Doctors'),
path('myservice/', views.myservice, name='myservice'),
path('appointment/', views.appointment, name='appointment'),
path('show/', views.show, name='show'),
]
