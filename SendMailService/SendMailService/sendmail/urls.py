from . import views
from django.urls import path, include

urlpatterns = [
    path('api/v1/sendmail', views.sendmail),
]
