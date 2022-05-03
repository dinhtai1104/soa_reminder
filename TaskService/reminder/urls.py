from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_note/', views.createNote, name="note" ) #add this 
]
