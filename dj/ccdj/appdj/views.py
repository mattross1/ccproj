from django.shortcuts import render
from django.http import HttpResponse
from .models import Food

# Create your views here.

def index(request):
    return HttpResponse("Test Response")

def getfoods(request):
    retdata = Food.objects.all()
    datavars={
        'foodobj':retdata
    }
    return render(request, 'favfoods.html', datavars)