from django.shortcuts import render
from Adminapp.serializers import Course_serializer,Staff_serializer,Student_serializer,Subject_serializer,Notification_Student_serializer,Notifiction_Staff_serializer,History_serializer
from Adminapp.models import Coursemodel,Staffmodel,Studentmodel,Subject_model,Notifiction_Student,Notifiction_Staff,History
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class CourseView(APIView):
      def get(self,request):
            detailobj=Coursemodel.objects.all().order_by('id')
            serializeobj=Course_serializer(detailobj,many=True)
            return Response(serializeobj.data)
      def post(self,request):
            serializeobj=Course_serializer(data=request.data)
            if(serializeobj.is_valid()):
                  serializeobj.save()
                  return Response(200)
            return Response(serializeobj.errors)
class UpdateCourse(APIView):
      def put(self,request,id):
            detailobj=Coursemodel.objects.get(id=id)
            serializeobj=Course_serializer(detailobj,data=request.data)
            if(serializeobj.is_valid()):
                  serializeobj.save()
                  return Response(serializeobj.data)
            return Response(serializeobj.errors)
class DeleteCourse(APIView):
      def delete(self,request,id):
            detailobj=Coursemodel.objects.get(id=id)
            detailobj.delete()
            return Response(200)
class CourseViewIndividual(APIView):
      def get(self,request,id):
            detailobj=Coursemodel.objects.all().filter(id=id)
            serializeobj=Course_serializer(detailobj,many=True)
            return Response(serializeobj.data)
                    
# .....................................................................................

class Staffgetview(APIView):
                    def get(self,request):
                          obj=Staffmodel.objects.all()
                          serializeobj=Staff_serializer(obj,many=True) 
                          return Response(serializeobj.data)
                    def post(self,request):
                            serialzerobj=Staff_serializer(data=request.data)
                            if serialzerobj.is_valid():
                                                serialzerobj.save() 
                            else:
                                  return Response(serialzerobj.errors)
                            return Response(200)  
class Updatestaff(APIView):
                    def put(self,request,id):
                                        obj=Staffmodel.objects.get(id=id)
                                        serializerobj=Staff_serializer(obj,data=request.data)                                     
                                        if(serializerobj.is_valid()):
                                               serializerobj.save()
                                        else:
                                              return Response(serializerobj.errors)
                                        return Response(200)
class Deletestaff(APIView):
                    def delete(self,request,id):
                             obj=Staffmodel.objects.get(id=id)
                             obj.delete()
                             return Response(200)                                                   
                    
class Staffindividual(APIView):
        def get(self,request,id):
              obj=Staffmodel.objects.filter(id=id)
              serializeobj=Staff_serializer(obj,many=True)
              return Response(serializeobj.data)   
# .........................................................................
class Studentgetview(APIView):
      def get(self,request):
            obj=Studentmodel.objects.all() 
            serializerobj=Student_serializer(obj,many=True) 
            return Response(serializerobj.data)                       
      def post(self,request):
            serializerobj=Student_serializer(data=request.data)
            if serializerobj.is_valid():
                   serializerobj.save()
            else:
                  return Response(serializerobj.errors) 
            return Response(200)
                               
class Updatestudent(APIView):
      def put(self,request,id):
            obj=Studentmodel.objects.get(id=id)
            serializeobj=Student_serializer(obj,data=request.data) 
            if serializeobj.is_valid():
                  serializeobj.save()
            else:
                  return Response(serializeobj.errors) 
            return Response(200)
                           
class Deletestudent(APIView):
      def delete(self,request,id):
            obj=Studentmodel.objects.get(id=id)
            obj.delete() 
            return Response(200)   
class StudentgetIndividual(APIView):
      def get(self,request,id):
            obj=Studentmodel.objects.filter(id=id)
            serializeobj=Student_serializer(obj,many=True) 
            return Response(serializeobj.data) 
class Studentget_Data_Registernumber(APIView):
      def get(self,request,id):
            obj=Studentmodel.objects.filter(registerno=id)
            serializeobj=Student_serializer(obj,many=True) 
            return Response(serializeobj.data)   
      
class Studentget_Data_Cousebased(APIView):
      def get(self,request,id):
          try:                    
            obj=Studentmodel.objects.all().filter(course=id)
            serializeobj=Student_serializer(obj,many=True) 
            return Response(serializeobj.data)
          except:
                return Response(400)        
# ..................................................................................
class Subjectview(APIView):
      def get(self,request):
            obj=Subject_model.objects.all()
            serializeobj=Subject_serializer(obj,many=True)
            return Response(serializeobj.data)
      def post(self,request):
                serializeobj=Subject_serializer(data=request.data) 
                if serializeobj.is_valid():
                        serializeobj.save()
                                
                else:
                    return Response(serializeobj.errors)                             
                                        
                return Response(200)                        
class Updatesubject(APIView):
      def put(self,request,id):
              obj=Subject_model.objects.get(id=id)
              serializeobj=Subject_serializer(obj,data=request.data)
              if serializeobj.is_valid():
                  serializeobj.save()
              else:
                    return Response(serializeobj.errors)
              return Response(200)                          
                                
class Deletesubjet(APIView):
      def delete(self,request,id):
            obj=Subject_model.objects.filter(id=id) 
            obj.delete()  
            return Response(200)         
      
class Subjectindividual(APIView):
      def get(self,request,id):                     
        obj=Subject_model.objects.filter(id=id)
        serializeobj=Subject_serializer(obj,many=True)
        return Response(serializeobj.data) 
# ..........................................................................

class NotificationstudentView(APIView):
      def get(self,request):
             obj=Notifiction_Student.objects.all()
             serializeobj=Notification_Student_serializer(obj,many=True)
             return Response(serializeobj.data)  
      def post(self,request):
            serializeobj=Notification_Student_serializer(data=request.data)
            # reg_field=request.data["registerno"]
            # status_field=request.data["status"]
            # obj=Notifiction_Student.objects.filter(registerno=reg_field).update(status=status_field)
            if(serializeobj.is_valid()):
                  serializeobj.save() 
                  return Response(200)                 
            else:
                 return Response (serializeobj.errors)
class Update_Student_Notif(APIView):
      def put(self,request,id):
            obj=Notifiction_Student.objects.get(id=id)
            serializeobj=Notification_Student_serializer(obj,data=request.data)
            if serializeobj.is_valid():
                  serializeobj.save()
                  return Response(200)
            else:
               return Response(serializeobj.errors)                                                   
           
class DeleteStudentnotification(APIView):
      def delete(self,request,id):
            obj=Notifiction_Student.objects.filter(id=id)
            obj.delete()
            return Response(200)           
class NotifictionStudentIndividual(APIView):
      def get(self,request,id):
                           
            obj=Notifiction_Student.objects.filter(registerno=id)
            serializeobj=Notification_Student_serializer(obj,many=True)
            return Response(serializeobj.data)   
      
#.................................................................................     
class Notification_StaffView(APIView):
      def get(self,request):
             obj=Notifiction_Staff.objects.all()
             serializeobj=Notifiction_Staff_serializer(obj,many=True)
             return Response(serializeobj.data)  
      def post(self,request):
            serializeobj=Notifiction_Staff_serializer(data=request.data)
            statusfield=request.data['status']
            regno=request.data['registerno']
           
          
           
            if(serializeobj.is_valid()):
                  serializeobj.save() 
                  return Response(200)                 
            else:
                  return Response (serializeobj.errors) 
              
class Update_Staff_Notif(APIView):
      def put(self,request,id):
            obj=Notifiction_Staff.objects.get(id=id)
            serializeobj=Notifiction_Staff_serializer(obj,data=request.data)
            if serializeobj.is_valid():
                  serializeobj.save()
                  return Response(200)
            else:
               return Response(serializeobj.errors)                                                        
           
class Delete_Staffnotification(APIView):
      def delete(self,request,id):
            obj=Notifiction_Staff.objects.filter(id=id)
            obj.delete()
            return Response(200)           
class NotifictionStaff_Individual(APIView):
    
        def get(self,request,id):
              obj=Staffmodel.objects.filter(staff_registerid=id)
              serializeobj=Staff_serializer(obj,many=True)
              return Response(serializeobj.data) 
# ....................................................................
class History_View(APIView):
      def get(self,request):
             obj=History.objects.all()
             serializeobj=History_serializer(obj,many=True)
             return Response(serializeobj.data)
class Delete_History(APIView):
      def delete(self,request,id):
            obj=History.objects.filter(id=id)
            obj.delete()
            return Response(200)             
            