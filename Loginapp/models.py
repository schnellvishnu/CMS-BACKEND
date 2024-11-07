from django.db import models

# Create your models here.
class Signinmodel(models.Model):
       id= models.AutoField(primary_key=True)
       staff_id=models.CharField(max_length=100,unique=True,default="false")
       name=models.CharField(max_length=100,null=True)
       age=models.IntegerField(null=True)
       address=models.TextField(max_length=100,null=True)
       phone=models.CharField(max_length=100,null=True)
       userrole=models.CharField(max_length=100,null=True)
       username=models.CharField(max_length=100,null=True,unique=True)
       password=models.CharField(max_length=100,null=True)
       
       def __str__(self):
                    return self.name  

       
       
       
                   