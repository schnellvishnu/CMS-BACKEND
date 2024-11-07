from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from Loginapp.models import Signinmodel
from Loginapp.serializers import SigninSerializer
# Create your views here.
class Loginview(APIView):
       def get(self,request):
               obj=Signinmodel.objects.all()
               serializeobj=SigninSerializer(obj,many=True)
               return Response(serializeobj.data)                     
       def post(self,request):
                    uname=request.data["username"]
                    passwor=request.data["password"]
                   
                    username=Signinmodel.objects.filter(username= uname).values()
                    
                    if username:
                                        
                         if(username[0]["password"]==passwor):
                                             
                                 
                    #              obj=Signinmodel.objects.get(username=uname) 
                    #              userrole=obj.userrole
                    #              print(userrole) 
                                 if username[0]["userrole"]=="admin":
                                         print("44444444444")
                                         return Response(100)
                                 elif(username[0]["userrole"]=="staff"):
                                         return Response(200)
                                          
                                 elif(username[0]["userrole"] =="student"):
                                        return Response(300)              
                         else:
                             return Response("Incorrect Password") 
                    else:
                         return Response("User Does Not Exist") 
                       
                                                              
class  Registerview(APIView):
        def post(self,request):
                serializebj=SigninSerializer(data=request.data)
                try:
                        uname=request.data["username"]
                        passwor=request.data["password"] 
                        regno=request.data['staff_id']
                        obj2=Signinmodel.objects.filter(staff_id=regno)
                        print(obj2[0])
                        if obj2[0] !="":
                          obj=Signinmodel.objects.filter(staff_id=regno).update( username=uname,password=passwor)
                          print("saved") 
                          return Response(200)
                except:
               
                        if serializebj.is_valid():
                                serializebj.save()
                                return Response(200)
                        else:
                                return Response(serializebj.errors) 
                                                                
                    
