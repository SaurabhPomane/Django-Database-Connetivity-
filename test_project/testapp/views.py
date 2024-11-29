
import json
from django.db import connection
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.db.models import Avg,Min,Max,Sum,Count
from testapp.form import StudentForm
from testapp.models import Employee, Student, User, UserData

# Create your views here.
def hellow(request):
    return HttpResponse ("this is my first function")
def hi(request):
    return HttpResponse ('this is second function')
def add(request):
    print(request)
    no1=request.GET["no1"]
    no2=request.GET["no2"]
    answer=int(no1)+int(no2)

    return render(request,"testapp/templates/operation.html",{'answer':answer,'no1':no1,'no2':no2})
def GiveMePage(request):
    return render (request,'testapp/templates/operation.html') 

# def giveMeRegister(request):
#     return render(request,"testapp/templates/register.html") 

def save(request):
    if request.method=="GET":
     return render(request,"testapp/templates/register.html")
    usernamefrombrouser=request.POST['username']
    passwordfrombrouser=request.POST['password']
    mobilefrombrouser=request.POST['mobno']
    UserData.objects.create(username=usernamefrombrouser,password=passwordfrombrouser,mobno=mobilefrombrouser)

    return render(request,"testapp/templates/login.html",{'message':'register successful'})  

def login(request):
    if request.method=="GET":
     return render(request,"testapp/templates/login.html")
    username_db=request.POST['username']
    password_db=request.POST['password']
    try:
     datafrom_db=UserData.objects.get(username=username_db)
    except:
       return render(request,"testapp/templates/login.html",{'message':'invalid username'})
    if datafrom_db.password==password_db:
     return render(request,"testapp/templates/homepage.html",{'message':'welcome' +" "+ username_db})  
    else:
            return render(request,"testapp/templates/login.html",{'message':'invalid password'})

def display_data(request):
   if request.method=='GET':
    listofDictionary=UserData.objects.all().values("username","mobno","password")
    return render(request,"testapp/templates/display.html/",{'listofDictionary':listofDictionary})
   
   usernamefrombr=request.POST["username"]
   if usernamefrombr!=" ":
      listofDictionary=UserData.objects.filter(username=usernamefrombr)
   return render(request,"testapp/templates/display.html/",{'listofDictionary':listofDictionary})  

def delete(request,usernamefrombrouser):
   
   UserData.objects.filter(username=usernamefrombrouser).delete()
   return display_data(request) 


def crudoperation(request):
   return render(request,"testapp/templates/crud.html")


def view(request):
   usernamebr=request.GET["username"]
   userdata=UserData()
   try:
      userdata=UserData.objects.get(username=usernamebr)
   except:
      return render(request,"testapp/templates/crud.html",{'message':'record not found'})   
   return render (request,"testapp/templates/crud.html",{'userdata':userdata})

def add(request):
    usernamefrombrouser=request.GET['username']
    passwordfrombrouser=request.GET['password']
    mobilefrombrouser=request.GET['mobno']
    UserData.objects.create(username=usernamefrombrouser,password=passwordfrombrouser,mobno=mobilefrombrouser)
    return render(request,"testapp/templates/crud.html",{'message':'added successfully'})

def update(request):
   userfrombr=request.GET["username"]
   userdata=UserData.objects.get(username=userfrombr)
   userdata.password=request.GET["password"]
   userdata.mobno=request.GET["mobno"]
   userdata.save()
   print(connection.queries)

   return render (request,"testapp/templates/crud.html",{'message':'update successfully'})

def delette(request):
   usernamefrombr=request.GET["username"]
   UserData.objects.filter(username=usernamefrombr).delete()
   return render  (request,"testapp/templates/crud.html",{'message':'delete successfully'})



def setSession(request):
   request.session["index"]=0
   return HttpResponse("session is set ")

def increase(request):
   request.session["index"]=request.session["index"]+1
   return HttpResponse(f"index value is {request.session['index']}")

def check(request):
 
    message="username already present"

    try:
        userdata=UserData.objects.get(username=request.GET["username"])
        print(userdata)
    except:
        message='username does not exist'

    dictionary={'message':message}

    jsondata=json.dumps(dictionary) # dumps() converts python dictionary into JSON String

    print(jsondata)

    response=HttpResponse(f'{jsondata}',content_type='application/json')
    
    return response


def aggration(request):
   # emp=Employee.objects.filter(Emp_salary__gt=200000)
   # emp=Employee.objects.filter(Emp_salary__lt=300000)
   emp=Employee.objects.filter(Emp_salary__range=(100000,400000))
   # emp=Employee.objects.filter(Emp_salary=200000)
   # emp=Employee.objects.filter(Emp_salary__isnull=True)
   # emp=Employee.objects.count()
   # emp=Employee.objects.aggregate(Avg('Emp_salary'))
   # emp=Employee.objects.aggregate(Min('Emp_salary'))
   # emp=Employee.objects.aggregate(Max('Emp_salary'))
   # emp=Employee.objects.aggregate(Sum('Emp_salary'))
   # emp=Employee.objects.aggregate(Count('Emp_id'))
   


   print (emp)
   print(connection.queries)
   return render (request,'testapp/templates/aggrations.html',{'emp':emp})


def saveUserData(request):
   
    if request.method=='GET':
        return render(request,'testapp/templates/registernew.html')
    
    print(type(request))
    name=request.POST['username']
    password=request.POST['password']
    mobno=request.POST['mobno']
    email=request.POST['email']
    filedata=request.FILES['photo']
    imagepath='/upload/'+filedata.name

    with open('testapp/static/upload/'+filedata.name, 'wb+') as destination:  
                for byte in filedata.chunks():  
                    destination.write(byte)

    
    User.objects.create(username=name,password=password,mobno=mobno,email=email,imagepath=imagepath)
   
    return render(request,'loginnew.html',{'message':'registration successful.please login now'})



def login2(request):
    
    if request.method=='GET':
        return render(request,"testapp/templates/loginnew.html")
    
    usernamefrombrowser=request.POST["username"]
    passwordfrombrowser=request.POST["password"]

    try:
        userfromdb=User.objects.get(username=usernamefrombrowser) 
    except:
        return render(request,"testapp/templates/loginnew.html",{'message':"invalid username"})

    if userfromdb.password==passwordfrombrowser:

        imagepath=userfromdb.imagepath

        return render(request,"testapp/templates/welcomenew.html",{"message":"welcome " + usernamefrombrowser ,"imagepath":imagepath})
    else:
        return render(request,"testapp/templates/loginnew.html",{'message':"invalid password"})
    

    

def generateForm(request):

    if request.method=="POST":

       form=StudentForm(request.POST)

       if form.is_valid():
            try:
               form.save()
               return redirect ("/testapp/show")
            except Exception as message:
                print(message)
    else:
        form=StudentForm()
    
    return render(request,"testapp/templates/student.html",{'form':form})


def show(request):  
    students = Student.objects.all()  
    return render(request,"testapp/templates/show.html",{'students':students})  