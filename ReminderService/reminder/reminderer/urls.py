from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/remind', views.remindFunction),
    path('', views.home),
]
