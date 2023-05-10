from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from meetings.models import Meeting,Room

def welcome(request):
    return render(request,"website/welcome.html",
                  {"meetings" : Meeting.objects.all()})

