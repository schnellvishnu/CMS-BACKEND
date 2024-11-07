from rest_framework import serializers
from Adminapp .models import Coursemodel,Staffmodel,Studentmodel,Subject_model,Notifiction_Student,Notifiction_Staff,History

class Course_serializer(serializers.ModelSerializer):
                    class Meta:
                       model=Coursemodel
                       fields="__all__"
                       
class Staff_serializer(serializers.ModelSerializer):
   class Meta:
         model=Staffmodel
         fields="__all__" 
         
class Student_serializer(serializers.ModelSerializer):
   class Meta:
      model=Studentmodel
      fields="__all__"                               
      
class Subject_serializer(serializers.ModelSerializer):
   class Meta:
      model=Subject_model
      # fields="__all__" 
      exclude=["time"]       
      
class Notification_Student_serializer(serializers.ModelSerializer):
   class Meta:
      model=Notifiction_Student
      fields="__all__" 
      
class Notifiction_Staff_serializer(serializers.ModelSerializer):
   class Meta:
      model=Notifiction_Staff
      fields="__all__"     
      
class History_serializer(serializers.ModelSerializer):
   class Meta:
      model=History
      fields="__all__"             
                 