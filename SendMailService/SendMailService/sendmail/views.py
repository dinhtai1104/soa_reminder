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

    title = request.data['title'] 
    date = request.data['deadline'] 
    email = request.data['email'] 
    message = request.data['message'] 
    # body_unicode = request.body.decode('utf-8') 	
    # body = json.loads(body_unicode) 	
    # content = body['content']

    # print(content)
    send_mail(
    'Deadline!!' + title,
    message,
    settings.EMAIL_HOST_USER,
    [email],
    fail_silently=False,
    )
    return HttpResponse('Sent!')

def sendmail1(request):
    send_mail(
    'Deadline!!',
    '?',
    settings.EMAIL_HOST_USER,
    ['dinhtai2000@gmail.com'],
    fail_silently=False,
    )
    return render(request, 'home.html')