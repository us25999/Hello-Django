
from django.http import HttpResponse
from django.shortcuts import render

from django.core.mail import send_mail
from twilio.rest import Client

from sendsms import api

from rest_framework.response import Response




 

       

def mail(request):
    if request.method == "POST":
        sub = request.POST.get('subject')
        msg = request.POST.get('message')
        email = request.POST.get('email')
        send_mail(
            sub,
            msg,
            'smtp259demo@gmail.com',
            [email],
            fail_silently=False,
        )
        return HttpResponse("mail sent successfully")
       
    return render(request,'mail_sender.html')


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
    


    
 
        
    
    
            

    


