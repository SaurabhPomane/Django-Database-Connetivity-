from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from secondapp.models import UserData

# Create your views here.
def first(request):
    return HttpResponse("this is a second app")
def calculator(request):
    num1= request.GET['no1']
    num2=request.GET['no2']
    if request.GET["op"] =='substraction':
     ans=int(num1) - int(num2)
    elif request.GET["op"]=="addition":
       ans=int(num1)+int(num2)
    elif request.GET["op"]=="multiplication":
       ans=int(num1)*int(num2)
    else:
       ans=int(num1)/int(num2)       

    return render(request,'secondapp/templates/calci.html',{'ans':ans,'no1':num1,'no2':num2} )
def result (request):
    return render(request,'secondapp/templates/calci.html')
   
def save(request): 
   if request.method=="GET" :
      return render(request,"secondapp/templates/register.html")
   usernamebr=request.POST["username"] 
   passwordbr=request.POST["password"]
   mobileno=request.POST["mono"]
   UserData.objects.create(username=usernamebr,password=passwordbr,mono=mobileno)
   return render(request,"secondapp/templates/login.html")

def login(request):
   if request.method=="GET":
      return render(request,"secondapp/templates/login.html")
   
   user=request.POST["username"]
   passwordd=request.POST["password"]
   try:
     register_data=UserData.objects.get(username=user) 
   except:
      return render(request,"secondapp/templates/login.html",{'message':'invalid username'})
   if register_data.password==passwordd:
      return render(request,"secondapp/templates/homepage.html",{'message':'welcome'+" "+ user}) 
   else:
      return render(request,"secondapp/templates/login.html",{'message':'invalid password'})  
   
def display(request):   
   data=UserData.objects.all().values("username","password","mono")
   return render (request,"secondapp/templates/displays.html",{"data":data})

def delete(request,usernamebr):
   UserData.objects.filter(username=usernamebr).delete()
   return display(request)

def crud_operation(request):
   if request.method=='GET':
    return render (request,"secondapp/templates/crud.html")
   

@api_view(["GET","POST"])
def givestudentdetail(request):
   return Response({'rno':1,"name":'sai'})