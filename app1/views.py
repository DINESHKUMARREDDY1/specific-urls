from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('<h1> Do your work PROPERLY</h1>')
def second(request):
    return HttpResponse('<marquee> CRICKET IS FAV GAME</marquee>')
