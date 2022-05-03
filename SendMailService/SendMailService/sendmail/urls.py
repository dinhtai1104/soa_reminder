from . import views
from django.urls import path, include

urlpatterns = [
    path('sendmail', views.sendmail),
    path('sendmail1/', views.sendmail1)
]
