from datetime import datetime
from email import message
from django.http import HttpResponse
from django.shortcuts import render
from meetings.models import Meeting

def welcome(request):
    return render(request,"website/welcome.html",
    {"messag":"This data was sent from the view to the templates","meeting":Meeting.objects.all()})

def date(request):
    return HttpResponse("this page is viewed at "+str(datetime.now()))

def AboutMe(request):
    return HttpResponse("Hi I am Nimish")