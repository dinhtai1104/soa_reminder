from re import sub
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.core.mail import send_mail
# Create your views here.

from django.conf import settings
import json
@api_view(['POST'])
def sendmail(request):
    print(request.data)
    print(request.POST.keys())

    nametask = request.data['nameTask'] 
    date = request.data['deadline'] 
    email = request.data['email'] 
    message = request.data['message'] 
    subject=request.data['subject']
    user=request.data['userCreate']
    alert=request.data['alert']

    # body_unicode = request.body.decode('utf-8') 	
    # body = json.loads(body_unicode) 	
    # content = body['content']

    # print(content)

    messageSent = "Chào " + user + ",\n" + "Bạn có một thông báo nhắc nhở công việc " + nametask + " vào " + date + "\n" + "Thông báo là: " + message
    messageEnd = "Chào " + user + ",\n" + "Bạn đã đến hạn phải thực hiện công việc " + nametask + "\n" + "Thông báo là: " + message
    
    if alert == "5mins":
        send_mail(
        subject=subject,
        message=messageSent,
        from_email= settings.EMAIL_HOST_USER,
        recipient_list= [email],
        fail_silently=False,
        )
    elif alert == "0mins":
        send_mail(
        subject=subject,
        message=messageEnd,
        from_email= settings.EMAIL_HOST_USER,
        recipient_list= [email],
        fail_silently=False,
        )
    return HttpResponse('Sent!')

''''
"nameTask" : self.taskname,
"userCreate" : self.user,
"subject" : self.subject,
"message" : self.message,
"email" : self.email,
"deadline" : self.date
'''