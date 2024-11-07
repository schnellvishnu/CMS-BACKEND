from django.db import models

# Create your models here.
class Coursemodel(models.Model):
      id= models.AutoField(primary_key=True)
      course_name=models.CharField(max_length=100,null=True)
      year=models.CharField(max_length=100,null=True)
      fees=models.IntegerField(null=True)
      description=models.TextField(max_length=1000,null=True)
      def __str__(self):
                    return self.course_name 

class Staffmodel(models.Model):
      id=models.AutoField(primary_key=True)
      staff_registerid=models.CharField(max_length=100,unique=True)
      staff_name=models.CharField(max_length=100,null=True)
      address=models.TextField(max_length=100,null=True)
      age=models.CharField(max_length=100,null=True)
      qualification=models.CharField(max_length=100,null=True)
      phone=models.IntegerField(null=True,default=False)
      # subject=models.CharField(max_length=100,null=True)
      staff_uname=models.CharField(max_length=100,null=True)
      staff_pwd=models.CharField(max_length=100,null=True)
      
      def __str__(self):
            return self.staff_name 
                    
class Studentmodel(models.Model):
      id=models.AutoField(primary_key=True) 
      registerno=models.CharField(max_length=100,null=True,unique=True)
      student_name=models.CharField(max_length=100,null=True)
      address=models.TextField(max_length=100,null=True) 
      age=models.IntegerField() 
      qualification=models.CharField(max_length=100)
      # grade=models.CharField(max_length=100) 
      phone=models.CharField(max_length=100,null=True)
      course=models.CharField(max_length=100,null=True)
      year=models.DateField(null=True)
      student_uname=models.CharField(max_length=100,null=True)
      student_pwd=models.CharField(max_length=100,null=True)
      def __str__(self):
            return self.student_name              
      
class Subject_model(models.Model):
      id= models.AutoField(primary_key=True)
      course=models.CharField(max_length=100,null=True)
      staff=models.CharField(max_length=100,null=True)
      time=models.DateTimeField(null=True)
      subject=models.CharField(max_length=100,null=True)
      def __str__(self):
            return self.subject 
      
class Notifiction_Student(models.Model):
      id=models.AutoField(primary_key=True)
      registerno=models.CharField(max_length=100,null=True)
      course=models.CharField(max_length=100,null=True)
      name=models.CharField(max_length=100,null=True)
      message=models.TextField(max_length=500,null=True) 
      status=models.CharField(max_length=100,null=True) 
      date=models.DateField(null=True)
      def __str__(self):
            return self.registerno   
      
class Notifiction_Staff(models.Model):
      id=models.AutoField(primary_key=True)
      registerno=models.CharField(max_length=100,null=True)
      course=models.CharField(max_length=100,null=True)
      name=models.CharField(max_length=100,null=True)
      message=models.TextField(max_length=500,null=True) 
      status=models.CharField(max_length=100,null=True)
      date=models.DateField(null=True) 
      def __str__(self):
            return self.registerno 
      
class History(models.Model):
    id=models.AutoField(primary_key=True) 
    modelname = models.CharField(max_length=100)
    savedid = models.CharField(max_length=100)
    operationdone = models.CharField(max_length=100)
    donebyuser = models.CharField(max_length=100)
    donebyuserrole = models.CharField(max_length=100)
    donedatetime = models.DateTimeField(max_length=100)
    description=models.CharField(max_length=300,default="True")
    donebyemployeeid=models.CharField(max_length=100,null=True)
    
    historyflag=models.BooleanField(default=False)
    def __str__(self):
        return self.donebyuser                  