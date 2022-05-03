from tkinter import Y
from unicodedata import name
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from reminder import models
import asyncio

from asgiref.sync import sync_to_async
from time import sleep
# Create your views here.
def index(request):

    return render(request, 'index.html')

def crunching_stuff():
    sleep(3)
    print("Woke up after 3 seconds!")
   
def createNote(request):
    if request.method == 'POST': 
        title = request.POST.get('title') 
        date = request.POST.get('deadline') 
        print(title)
        models.Task.objects.create(
            nameTask=title,
            deadline=date
        )
        # import threading
        # t = threading.Thread(target=crunching_stuff, args=(), kwargs={})
        # t.setDaemon(True)
        # t.start()

    return JsonResponse({"status": 'Success'}) 
 
