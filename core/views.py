from django.shortcuts import render,redirect
from django.http import HttpResponse
import json
from .writemodel import *
from django.http import JsonResponse
import os
import subprocess
from django.apps import apps


def home(request):
    return HttpResponse("<div style='text-align: center;margin-top: 50px;'><h1>The install worked successfully! Congratulations! </h1></div>")


def createDB(request):
    # start create models.py function and logic
    app_name = 'core'
    app_models = apps.get_app_config(app_name).get_models()
    model_names = [model.__name__ for model in app_models]
    context_data = {
        'models':model_names
    }
    models = json.dumps(context_data)

    if request.method == 'POST':
        tablename = request.POST.get('tablename')
        fieldArry = request.POST.get('fieldArry')
        fields = json.loads(fieldArry)
        is_writemodel = writeModel(tablename, fields)
        response_data = None
        if is_writemodel == True:
            response_data = { 
                'message': 'Data Table created successfully', 'status': 'success'}
        else:
            response_data = {'status': 'failed'}
        return JsonResponse(response_data)
    return render(request, 'db/index.html',{'context': models})


def loading(request):
     # Run makemigrations
    subprocess.run(['python', 'manage.py', 'makemigrations'], check=True, stderr=subprocess.PIPE)
    # Run migrate
    subprocess.run(['python', 'manage.py', 'migrate'], check=True, stderr=subprocess.PIPE)
    return render(request,'db/loading.html')

def showtable(request):
    app_name = 'core'
    app_models = apps.get_app_config(app_name).get_models()
    model_names = [model.__name__ for model in app_models]
    context = {
        'model_names':model_names
    }
    return render(request,'db/showtable.html',context)