
from django.http import HttpResponse
from django.shortcuts import render

from django.core.mail import send_mail
from twilio.rest import Client
from rest_framework.decorators import api_view

from sendsms import api

from rest_framework.response import Response




 

       
@api_view(['POST'])
def mail(request):
    if request.method == "POST":
        email = request.data['email']
        sub = 'Welcome to RDSO'
        msg = 'You have succesafully registerd. You will be provided password post verification by directed admin of RDSO.'
        send_mail(
            sub,
            msg,
            'smtp259demo@gmail.com',
            [email],
            fail_silently=False,
        )
        return HttpResponse("mail sent successfully")
    


def sms(request):
    if request.method == "POST":
        msg = request.POST.get('message')
        mob = request.POST.get('sendto')
        account_sid = 'AC9410ba5fcaafbf703cd17e413167338f'
        auth_token = 'edb065a617ce7f9bae9987f63394a7d6'
        client = Client(account_sid, auth_token)


        message = client.messages\
                        .create(
                            body=msg,
                            from_='+15053915515',
                            to="+91"+ mob
                        )
        return HttpResponse("sms sent successfully")
    return render(request,'sms_sender.html') 
    


    
 
        
    
    
            

    


