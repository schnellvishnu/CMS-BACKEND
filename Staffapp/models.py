from django.db import models

# Create your models here.
class Attendance_Maths(models.Model):
      id= models.AutoField(primary_key=True)
      regno=models.CharField(max_length=100,default=False)
      course=models.CharField(max_length=100,null=True)
      subject=models.CharField(max_length=100,null=True)
      date=models.DateField(null=True)
      name=models.CharField(max_length=100,null=True)
      status=models.CharField(max_length=100,null=True)
      # attendance=models.JSONField(default={'Name':'null', 'Attendance': 'Present', }) 
      def __str__(self):
                    return self.course
              
class Attendance_Eng(models.Model):
      id= models.AutoField(primary_key=True)
      regno=models.CharField(max_length=100,default=False)
      course=models.CharField(max_length=100,null=True)
      subject=models.CharField(max_length=100,null=True)
      date=models.DateField(null=True)
      name=models.CharField(max_length=100,null=True)
      status=models.CharField(max_length=100,null=True)
      # attendance=models.JSONField(default={'Name':'null', 'Attendance': 'Present', }) 
      def __str__(self):
                    return self.course  
              
class Attendance_Malay(models.Model):
      id= models.AutoField(primary_key=True)
      regno=models.CharField(max_length=100,default=False)
      course=models.CharField(max_length=100,null=True)
      subject=models.CharField(max_length=100,null=True)
      date=models.DateField(null=True)
      name=models.CharField(max_length=100,null=True)
      status=models.CharField(max_length=100,null=True)
      # attendance=models.JSONField(default={'Name':'null', 'Attendance': 'Present', }) 
      def __str__(self):
                    return self.course
              
class Attendance_Phy(models.Model):
      id= models.AutoField(primary_key=True)
      regno=models.CharField(max_length=100,default=False)
      course=models.CharField(max_length=100,null=True)
      subject=models.CharField(max_length=100,null=True)
      date=models.DateField(null=True)
      name=models.CharField(max_length=100,null=True)
      status=models.CharField(max_length=100,null=True)
      # attendance=models.JSONField(default={'Name':'null', 'Attendance': 'Present', }) 
      def __str__(self):
                    return self.course
              
class Attendance_Che(models.Model):
      id= models.AutoField(primary_key=True)
      regno=models.CharField(max_length=100,default=False)
      course=models.CharField(max_length=100,null=True)
      subject=models.CharField(max_length=100,null=True)
      date=models.DateField(null=True)
      name=models.CharField(max_length=100,null=True)
      status=models.CharField(max_length=100,null=True)
      # attendance=models.JSONField(default={'Name':'null', 'Attendance': 'Present', }) 
      def __str__(self):
                    return self.course    
              
class Attendance_Account(models.Model):
      id= models.AutoField(primary_key=True)
      regno=models.CharField(max_length=100,default=False)
      course=models.CharField(max_length=100,null=True)
      subject=models.CharField(max_length=100,null=True)
      date=models.DateField(null=True)
      name=models.CharField(max_length=100,null=True)
      status=models.CharField(max_length=100,null=True)
      # attendance=models.JSONField(default={'Name':'null', 'Attendance': 'Present', }) 
      def __str__(self):
                    return self.course   
              
class Attendance_History(models.Model):
      id= models.AutoField(primary_key=True)
      regno=models.CharField(max_length=100,default=False)
      course=models.CharField(max_length=100,null=True)
      subject=models.CharField(max_length=100,null=True)
      date=models.DateField(null=True)
      name=models.CharField(max_length=100,null=True)
      status=models.CharField(max_length=100,null=True)
      # attendance=models.JSONField(default={'Name':'null', 'Attendance': 'Present', }) 
      def __str__(self):
                    return self.course    
              
class All_Attendance(models.Model):
      id= models.AutoField(primary_key=True)
      regno=models.CharField(max_length=100,default=False)
      course=models.CharField(max_length=100,null=True)
      subject=models.CharField(max_length=100,null=True)
      date=models.DateField(null=True)
      name=models.CharField(max_length=100,null=True)
      status=models.CharField(max_length=100,null=True)
      # attendance=models.JSONField(default={'Name':'null', 'Attendance': 'Present', }) 
      def __str__(self):
                    return self.course   
class AddResult(models.Model):
      id= models.AutoField(primary_key=True)
      regno=models.CharField(max_length=100,default=False)
      course=models.CharField(max_length=100,null=True)
      name=models.CharField(max_length=100,null=True)
      subject=models.CharField(max_length=100,null=True)
      date=models.DateField(null=True)
      mark= models.CharField(max_length=100,null=True)
      grade=models.CharField(max_length=100,null=True)
      status=models.CharField(max_length=100,null=True)
      def __str__(self):
                  return self.course   

class ApplyStaffLeave(models.Model):
      id= models.AutoField(primary_key=True)
      regno=models.CharField(max_length=100,default=False)
      course=models.CharField(max_length=100,null=True)
      name=models.CharField(max_length=100,null=True)
      subject=models.CharField(max_length=100,null=True)
      date_on=models.DateField(null=True)
      date_to=models.DateField(null=True)
      message= models.CharField(max_length=100,null=True)
      status=models.CharField(max_length=100,null=True)   
      
class Apply_Student_Leave(models.Model):
      id= models.AutoField(primary_key=True)
      regno=models.CharField(max_length=100,null=True)
      course=models.CharField(max_length=100,null=True)
      name=models.CharField(max_length=100,null=True)
      subject=models.CharField(max_length=100,null=True)
      date_on=models.DateField(null=True)
      date_to=models.DateField(null=True)
      message= models.CharField(max_length=100,null=True)
      status=models.CharField(max_length=100,null=True)            
               
                                                                                                   