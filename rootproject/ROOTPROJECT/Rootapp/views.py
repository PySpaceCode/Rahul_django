from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    return HttpResponse("<h1>This is my irst views</h1>")

def index(request):
    d1={
        "name":"rahul",
        "age":21
        }
    return render(request,"Rootapp/index.html",context=d1)