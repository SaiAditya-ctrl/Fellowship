from django.shortcuts import render
import json
from . import tokens

import jwt

# Create your views here.
def index(request):
    return render(request,'index.html')

def registration(request):
    return render(request,'registration.html')

def saving(request):
    name=request.GET['name']
    password=request.GET['password']
   

    dic={"name":name,
         "password":password}
    f=open("data12.json",'r')
    s=json.load(f)
    f.close()
    s["User"].append(dic)
    f=open("data12.json",'w')
    json.dump(s,f)
    f.close()
    return render(request,'index.html',{'name':name,
                                        'password':password})
def login(request):
    return render(request,'login.html')
def func(request):
    name=request.GET['name']
    password=request.GET['password']
    token=tokens.token_activation(name,password)
    print(token)
    f=open("data12.json",'r')
    contents=json.load(f)
    for i in contents["User"]:
        if(name==i["name"] and password==i["password"]):
            return render(request,'dashboard.html',{'name':name})
        else:
            return not_found(request)
def not_found(request):
    return render(request,'login2.html')
