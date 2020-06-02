from django.http import HttpResponse
from django.http import  HttpResponseRedirect
from django.shortcuts import render
def home(request):
    return HttpResponse("<h1>this is awesome</h1>")
def form (request):
    return  render(request,'form.html')
def wcount(request):

    return  render(request,'count.html')