from django.db import models

# Create your models here.
class UserData(models.Model):
    username=models.CharField(max_length=20,primary_key=True)
    password=models.CharField(max_length=20)
    mono=models.BigIntegerField()


    class Meta:
        db_table="register_data"