from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse("Rcb WON THE CUP")
def second(request):
    return HttpResponse("CSK WON THE CUP")