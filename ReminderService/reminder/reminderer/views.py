from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
import threading
import time
from datetime import date, datetime
import asyncio
import requests

def home(request):
    return render(request, 'home.html')
@api_view(['POST'])
def index(request):
    title = request.POST.get('title') 
    date = request.POST.get('deadline') 
    email = request.POST.get('email') 
    message = request.POST.get('message') 
    print(datetime.now().date())


    value = datetime.now().date() 

    date_time = value.strftime("%Y-%m-%d")

    createNoteRemind(title, date, email, message, request)
    return render(request, 'home.html')


class myThread (threading.Thread):
    def __init__(self, taskname, date, email, message, request):
        # print(datetime.today().date)
        threading.Thread.__init__(self)
        self.taskname = taskname
        self.date = date
        self.email = email
        self.message = message
        self.request = request
    def run(self):
        while True:
            value = datetime.now().date() 

            date_time = value.strftime("%Y-%m-%d")
            print(date_time)

            if date_time == self.date:
                context = {'title': self.taskname, 'deadline': self.date, 'email': self.email, 'message': self.message}
                print("oke")

                self.sendmail(self.request, context)
                return
    def sendmail(self, request, context):
        import json
        resp = requests.post('http://127.0.0.1:9999/sendmail', data = json.dumps(context), headers={"Content-Type":"application/json"})
        print(resp.text)
        return render(request, 'sendmail.html', context)
        # return HttpResponse('Hello, async world!')
def createNoteRemind(taskname, date, email, message, request):
    remind=myThread(taskname=taskname, date=date, email=email, request=request, message=message)
    remind.start()
    pass