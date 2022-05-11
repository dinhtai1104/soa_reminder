from re import sub
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
import threading
import time
from datetime import datetime, timedelta
import asyncio
import requests

from reminderer.models import TaskModel

def home(request):
    return render(request, 'home.html')
@api_view(['POST'])
def remindFunction(request):
    subject = request.POST.get('subject') 
    date = request.POST.get('deadline') 
    email = request.POST.get('email') 
    message = request.POST.get('message') 
    task = request.POST.get('task')
    user = request.POST.get('user')

    createNoteRemind(user, task, subject, date, email, message, request)
    return render(request, 'home.html')


class myThread (threading.Thread):
    def __init__(self, user, taskname,subject, date, email, message, request):
        # print(datetime.today().date)
        threading.Thread.__init__(self)
        self.user = user
        self.subject = subject
        self.taskname = taskname
        self.date = date
        self.email = email
        self.message = message
        self.request = request

    def run(self):
        self.deadline = datetime.strptime(self.date, '%Y-%m-%dT%H:%M')
        print(self.deadline)
        print(datetime.now())
        isAlert5min = False
        alert = "5mins"

        while True:
            value = datetime.now() + timedelta(hours=7) 

            # date_time = value.strftime("%Y-%m-%d")

            minutes_diff = (self.deadline - value).total_seconds() / 60.0
            isAlert = False
            # print(minutes_diff)

            if minutes_diff< 5 and isAlert5min == False:
                alert = "5mins"
                isAlert5min = True
                isAlert = True
            elif minutes_diff <= 1 and isAlert5min == True:
                alert = "0mins"
                isAlert = True
            if isAlert == True:
                context = {
                    "nameTask" : self.taskname,
                    "userCreate" : self.user,
                    "subject" : self.subject,
                    "message" : self.message,
                    "email" : self.email,
                    "deadline" : self.date,
                    "alert": alert
                    }
                print("oke")
                isAlert = False
                self.sendmail(self.request, context)
                if alert == "0mins":
                    return
    def sendmail(self, request, context):
        import json
        resp = requests.post('http://127.0.0.1:9999/api/v1/sendmail', data = json.dumps(context), headers={"Content-Type":"application/json"})
        print(resp.text)
        return resp
        # return HttpResponse('Hello, async world!')
def createNoteRemind(user,taskname, subject, date, email, message, request):
        
    TaskModel.objects.create(
        nameTask = taskname,
        userCreate = user,

        subject = subject,
        message = message,
        email = email,
        deadline = date
        )
    remind=myThread(user=user, subject=subject,taskname=taskname, date=date, email=email, request=request, message=message)
    remind.start()
    pass