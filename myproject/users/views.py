from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #return HttpResponse("欢迎访问用户首页")
    return render(request,'home.html')
