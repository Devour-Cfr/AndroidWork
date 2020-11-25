from django.forms.models import model_to_dict
from django.shortcuts import render
from django.http import HttpResponse
import json
from FirstApp import models
# Create your views here.
def index(request):
    if(request.method == 'GET'):
        return render(request,'index.html')
    else:
        if(request.method == 'POST'):
            postBody = request.body
            data = json.loads(postBody)
            if data['action']=="1":
                try:
                    number = order(data)
                    return HttpResponse("预约成功，您的预约单编号为{}".format(number)) 
                except:
                    return HttpResponse("预约失败")
            elif data['action']=="2":
                try:
                    register(data)
                    return HttpResponse("注册成功") 
                except:
                    return HttpResponse("注册失败") 
            elif data['action']=="3":
                try:
                    receive(data)
                    return HttpResponse("接单成功") 
                except:
                    return HttpResponse("接单失败")
            elif data['action']=="4":
                try:
                    lst = query(data)
                    return HttpResponse(lst,"查询成功")
                except :
                    return HttpResponse("查询失败")
            else:
                print(postBody)
                return HttpResponse("嗯？")

def register(data):
    del data['action']
    print(data)
    models.register_list.objects.create(**data)

def order(data):
    del data['action']
    print(data)
    number = models.reservation_list.objects.create(**data).id
    #print(type(number))
    return number

def receive(data):
    print(data)

def query(data):
    del data['action']
    lst = models.reservation_list.objects.filter(phone=data['phone'])
    lst_dict = model_to_dict(lst[0])
    return json.dumps(lst_dict)
