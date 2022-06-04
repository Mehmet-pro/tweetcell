import json
from django.shortcuts import render
from django.http import HttpResponse
from .models import Likee


def index(request):
    data = Likee.objects.all()
    dic_data = {"active":f"{data[0].active}"}
    json_active = json.dumps(dic_data)
    return HttpResponse(json_active)