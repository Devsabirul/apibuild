from django.shortcuts import render
from django.http import HttpResponse
import json
from .witemodels import *
from django.http import JsonResponse


def home(request):
    return HttpResponse("<div style='text-align: center;margin-top: 50px;'><h1>The install worked successfully! Congratulations! </h1></div>")


def createDB(request):
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
    return render(request, 'db/index.html')
