from django.shortcuts import render
from django.http import HttpResponse

def home(request):
  return HttpResponse("<div style='text-align: center;margin-top: 50px;'><h1>The install worked successfully! Congratulations! </h1></div>")


def createDB(request):
  return render(request,'db/index.html')