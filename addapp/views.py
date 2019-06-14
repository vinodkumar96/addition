from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def input(request):
    return render(request,"base.html")
def add(request):
    v1=request.GET["t1"]
    v2=request.GET["t2"]
    a=int(v1)
    b=int(v2)
    c=a+b
    return HttpResponse("the sum is : " +str(c))
