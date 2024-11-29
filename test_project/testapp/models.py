from django.db import models

# Create your models here.

class UserData(models.Model):
    username=models.CharField(max_length=20,primary_key=True)
    password=models.CharField(max_length=30)
    mobno=models.IntegerField()
    
    def __str__(self) -> str:
        return (f"username is {self.username} and password is {self.password} and mobile no is {self.mobno}")
   
    class Meta:
        db_table="userdata"  


class Employee(models.Model):
    Emp_id=models.IntegerField(primary_key=True)
    Emp_name=models.CharField(max_length=20)
    Emp_salary=models.BigIntegerField()
    
    def __str__(self) :
        return f"eid is {self.Emp_id} and name is {self.Emp_name} and salary is {self.Emp_salary}"
    
    class Meta:
      db_table="employee"


class User(models.Model):

     username=models.CharField(max_length=20,primary_key=True)
     password=models.CharField(max_length=50)
     mobno = models.IntegerField()
     email=models.CharField(max_length=50)
     imagepath=models.CharField(max_length=50)
          
     #__str__() function gives us object data .

     def __str__(self):
          return "{},{},{},{},{}".format(self.username,self.password,self.mobno,self.email,self.imagepath)

     class Meta:
          db_table="user"


class Student(models.Model):

   rno = models.IntegerField(primary_key=True)
   marks = models.IntegerField()
   
   class Meta:
      db_table = "studdent"

