from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return HttpResponse("<h1>this is awesome</h1>")
def form (request):
    return  render(request,'form.html')
def wcount(request):
    data=request.GET['textarea'].split()
    word_Len=len(data)
    return  render(request,'count.html',{'data':word_Len})