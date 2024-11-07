from django.shortcuts import render
from Staffapp.models import Attendance_History,Attendance_Account,Attendance_Che,Attendance_Phy,Attendance_Eng,Attendance_Malay,Attendance_Maths,All_Attendance,AddResult,ApplyStaffLeave,Apply_Student_Leave
from Staffapp.serializers import Attendanceaccount_serializer,Attendancechy_serializer,Attendanceeng_serializer,Attendancemaths_serializer,Attendancephy_serializer,Attendancehistory_serializer,Attendancemal_serializer,All_Attendance_serializer,AddResult_serializer,ApplyLeave_serializer,Apply_Student_Leave_serializer
from Adminapp.models import History
from rest_framework.views import APIView
from rest_framework.response import Response
import datetime
# Create your views here.
class Attendance_MATHS_get(APIView):
       def get(self,request):
                obj=Attendance_Maths.objects.all()
                serializeobj=Attendancemaths_serializer(obj,many=True)
                return Response(serializeobj.data) 
       def post(self,request):
                 serializeobj=Attendancemaths_serializer(data=request.data) 
                 st_name=request.data["name"]
                 st_date=request.data["date"]
                 try:
                     dateobj=Attendance_Maths.objects.filter(date=st_date).filter(name=st_name)
                     # print(dateobj[0].name)
                     if(dateobj[0].name!=[]):
                            return Response("allready exist")
                     else:
                            if(serializeobj.is_valid()):
                                          serializeobj.save()
                                          return Response(200)
                            else:
                                   return Response(serializeobj.errors) 
                 except:
                     print("try not working")
                     if(serializeobj.is_valid()):
                            serializeobj.save()
                            return Response(200)
                     else:
                            return Response(serializeobj.errors) 
                        
                      
class DeleteAttendance_MATHS_view(APIView):
       def delete(self,request,id):
            obj=Attendance_Maths.objects.get(regno=id)
            obj.delete()
            return Response(200)    
 #  ...........................................................................
class Attendance_ENG_get(APIView):
       def get(self,request):
                obj=Attendance_Eng.objects.all()
                serializeobj=Attendanceeng_serializer(obj,many=True)
                return Response(serializeobj.data) 
       def post(self,request):
                 serializeobj=Attendanceeng_serializer(data=request.data) 
                 st_name=request.data["name"]
                 st_date=request.data["date"]
                 try:
                     deateobj=Attendance_Eng.objects.filter(date=st_date).filter(name=st_name)
                     print(deateobj[0].name)
                     if(deateobj!=[]):
                            return Response("allready exist")
                     else:                    
                            if(serializeobj.is_valid()):
                                          serializeobj.save()
                                          return Response(200)
                            else:
                                   return Response(serializeobj.errors) 
                 except:
                            if(serializeobj.is_valid()):
                                   serializeobj.save()
                                   return Response(200)
                            else:
                                   return Response(serializeobj.errors)           
class DeleteAttendance_ENG_view(APIView):
       def delete(self,request,id):
            obj=Attendance_Eng.objects.get(regno=id)
            obj.delete()
            return Response(200)    
# ..........................................................................
class Attendance_MALAYALAM_get(APIView):
       def get(self,request):
                obj=Attendance_Malay.objects.all()
                serializeobj=Attendancemal_serializer(obj,many=True)
                return Response(serializeobj.data) 
       def post(self,request):
                 serializeobj=Attendancemal_serializer(data=request.data) 
                 st_name=request.data["name"]
                 st_date=request.data["date"]
                 try:
                     # obj=Attendance_Malay.objects.get(name=st_name)
                     dateobj=Attendance_Malay.objects.filter(date=st_date).filter(name=st_name)
                     print(dateobj[0].name)
                     if dateobj!=[]:
                            return Response("allready exist") 
                     else:                   
                            if(serializeobj.is_valid()):
                                          serializeobj.save()
                                          return Response(200)
                            else:
                                   return Response(serializeobj.errors)                     
                 except:
                     print("hello")              
                 
                     
                                 
                     if(serializeobj.is_valid()):
                                   serializeobj.save()
                                   return Response(200)
                     else:
                            return Response(serializeobj.errors) 
                             
class DeleteAttendance_MALAYALAM_view(APIView):
       def delete(self,request,id):
            obj=Attendance_Malay.objects.get(regno=id)
            obj.delete()
            return Response(200)    
# ..............................................................................
class Attendance_PHY_get(APIView):
       def get(self,request):
                obj=Attendance_Phy.objects.all()
                serializeobj=Attendancephy_serializer(obj,many=True)
                return Response(serializeobj.data) 
       def post(self,request):
                 serializeobj=Attendancephy_serializer(data=request.data)
                 st_name=request.data["name"]
                 st_date=request.data["date"] 
                 try:
                     dateobj=Attendance_Phy.objects.filter(date=st_date).filter(name=st_name)
                     if(dateobj[0].name !=[]):
                            return Response("allready exist")  
                     else:  
                                          

                            if(serializeobj.is_valid()):
                                          serializeobj.save()
                                          return Response(200)
                            else:
                                   return Response(serializeobj.errors) 
                 except:
                     if(serializeobj.is_valid()):
                            serializeobj.save()
                            return Response(200)
                     else:
                            return Response(serializeobj.errors)               
class DeleteAttendance_PHY_view(APIView):
       def delete(self,request,id):
            obj=Attendance_Phy.objects.get(regno=id)
            obj.delete()
            return Response(200)    
#...........................................................................  
class Attendance_CHE_get(APIView):
       def get(self,request):
                obj=Attendance_Che.objects.all()
                serializeobj=Attendancechy_serializer(obj,many=True)
                return Response(serializeobj.data) 
       def post(self,request):
                 serializeobj=Attendancechy_serializer(data=request.data) 

                 st_name=request.data["name"]
                 st_date=request.data["date"] 
                 try:
                     dateobj=Attendance_Che.objects.filter(date=st_date).filter(name=st_name)
                     if(dateobj[0].name !=[]):
                            return Response("allready exist")  
                     else:  
                                          

                            if(serializeobj.is_valid()):
                                          serializeobj.save()
                                          return Response(200)
                            else:
                                   return Response(serializeobj.errors) 
                 except:
                     if(serializeobj.is_valid()):
                            serializeobj.save()
                            return Response(200)
                     else:
                            return Response(serializeobj.errors)
                             
class DeleteAttendance_CHE_view(APIView):
       def delete(self,request,id):
            obj=Attendance_Che.objects.get(regno=id)
            obj.delete()
            return Response(200)    
# ..........................................................................
class Attendance_ACCOUNT_get(APIView):
       def get(self,request):
                obj=Attendance_Account.objects.all()
                serializeobj=Attendanceaccount_serializer(obj,many=True)
                return Response(serializeobj.data) 
       def post(self,request):
                 serializeobj=Attendanceaccount_serializer(data=request.data) 

                 st_name=request.data["name"]
                 st_date=request.data["date"] 
                 try:
                     dateobj=Attendance_Account.objects.filter(date=st_date).filter(name=st_name)
                     if(dateobj[0].name !=[]):
                            return Response("allready exist")  
                     else:  
                                          

                            if(serializeobj.is_valid()):
                                          serializeobj.save()
                                          return Response(200)
                            else:
                                   return Response(serializeobj.errors) 
                 except:
                     if(serializeobj.is_valid()):
                            serializeobj.save()
                            return Response(200)
                     else:
                            return Response(serializeobj.errors)
                             
class DeleteAttendance_ACCOUNT_view(APIView):
       def delete(self,request,id):
            obj=Attendance_Account.objects.get(regno=id)
            obj.delete()
            return Response(200) 
     
# ..........................................................................
class Attendance_HISTORY_get(APIView):
       def get(self,request):
                obj=Attendance_History.objects.all()
                serializeobj=Attendancehistory_serializer(obj,many=True)
                return Response(serializeobj.data) 
       def post(self,request):
                 serializeobj=Attendancehistory_serializer(data=request.data) 

                 st_name=request.data["name"]
                 st_date=request.data["date"] 
                 try:
                     dateobj=Attendance_History.objects.filter(date=st_date).filter(name=st_name)
                     if(dateobj[0].name !=[]):
                            return Response("allready exist")  
                     else:  
                                          

                            if(serializeobj.is_valid()):
                                          serializeobj.save()
                                          return Response(200)
                            else:
                                   return Response(serializeobj.errors) 
                 except:
                     if(serializeobj.is_valid()):
                            serializeobj.save()
                            return Response(200)
                     else:
                            return Response(serializeobj.errors)
                             
class DeleteAttendance_HISTORY_view(APIView):
       def delete(self,request,id):
            obj=Attendance_History.objects.get(regno=id)
            obj.delete()
            return Response(200)  
     
# ..........................................................................
class All_Attendance_get(APIView):
       def get(self,request):
                obj=All_Attendance.objects.all()
                serializeobj=All_Attendance_serializer(obj,many=True)
                return Response(serializeobj.data) 
       def post(self,request):
                 serializeobj=All_Attendance_serializer(data=request.data) 


                 st_date=request.data["date"] 
                 st_subject=request.data["subject"]
                 st_coure=request.data["course"]
                 st_name=request.data["name"]
                 print( st_subject)
                 try:
                     dateobj=All_Attendance.objects.filter(date=st_date).filter(name=st_name).filter(subject=st_subject).filter(course=st_coure)
                     print(dateobj[0].subject)
                     if(dateobj[0].name !=[]):
                            print(dateobj[0].name)                    
                            return Response("allready exist")  
                     else:  
                                          

                            if(serializeobj.is_valid()):
                                   serializeobj.save()
                                   return Response(200)
                            else:
                                   return Response(serializeobj.errors) 
                 except:
                     if(serializeobj.is_valid()):
                            serializeobj.save()
                            return Response(200)
                     else:
                            return Response(serializeobj.errors)
                             
class Delete_All_Attendance__view(APIView):
       def delete(self,request,id):
            obj=All_Attendance.objects.filter(regno=id)
            obj.delete()
            return Response(200)  
     
class Attendance_viewpage_post(APIView):
       def get(self,request):
              obj=All_Attendance.objects.all()
              serializeobj=All_Attendance_serializer(obj,many=True)
              return Response(serializeobj.data) 
       def post(self,request):
              #    serializeobj=All_Attendance_serializer(data=request.data) 


                 st_date=request.data["date"] 
                 st_subject=request.data["subject"]
                 st_coure=request.data["course"]
              #    print(st_date)
              #    print(st_subject)
              #    print(st_coure)
                 try:
                     dateobj=All_Attendance.objects.filter(date=st_date).filter(subject=st_subject).filter(course=st_coure)
                     print(dateobj)
                     # return Response(200)
                     serializeobj=All_Attendance_serializer(dateobj,many=True)
                     if(dateobj !=[]):
                            print(200)                    
                            return Response(serializeobj.data)  
                     else:  
                                          
                            print("lp")
                            return Response("serializeobj.errors") 
                 except:
                    
                     print("kl")
                     return Response("serializeobj.errors") 
              
class Attendanceindividulaview(APIView):
       def get(self,request,id):
              obj=All_Attendance.objects.filter(id=id)
              serializeobj=All_Attendance_serializer(obj,many=True)
             
              return Response(serializeobj.data) 
class Update_Attendance(APIView):
       def put(self,request,id):
              obj=All_Attendance.objects.get(id=id)
              serializeobj=All_Attendance_serializer(obj,data=request.data)
              if serializeobj.is_valid():
                     serializeobj.save()
                     return Response(200)
              else:
                    return Response(500)                      
                                   
              
class Addreaultview(APIView):
       def get(self,request):
              obj= AddResult.objects.all()
              serializeobj=AddResult_serializer(obj,many=True)
              return Response(serializeobj.data)  
       def post(self,request):
                                  
                serializeobj=AddResult_serializer(data=request.data)
                if serializeobj.is_valid():
                     device=serializeobj.save()
                     subject=request.data["subject"]
                     name=request.data["name"]
                     date=request.data["date"]
                     registernumber=request.data["regno"]
                     historysave=History(modelname= registernumber,
                                savedid=device.id,
                                operationdone='Added Result',
                                donebyuser=request.data['loggedInUsername'],
                                donebyuserrole=request.data['loggedInUserrole'],
                                description="Added" + "\t" + subject + "\t" + "Result of Student" + "\t" + name + "\t"+"in" + date ,
                                donedatetime=datetime.datetime.now())
                     historysave.save()
                     return Response(200)
                else:
                       return Response(serializeobj.errors)  
                
class Updateresultview(APIView):
      def put(self,request,id):                     
         obj=AddResult.objects.get(id=id)
         serializeobj=AddResult_serializer(obj,data=request.data)
         subject=request.data["subject"]
         name=request.data["name"]
         date=request.data["date"] 
         registernumber=request.data["regno"]
         userole=request.data["loggedInUserrole"]
         if(serializeobj.is_valid()):
              device =serializeobj.save()
              historysave=History(modelname=registernumber,
                                savedid=device.id,
                                operationdone='Edit Result',
                                donebyuser=request.data['loggedInUsername'],
                                donebyuserrole=request.data['loggedInUserrole'],
                                description= "student" +  "\t"  + name + "\t" + subject + "\t" "Result Has Been Edited" + "\t" +  "in " + "\t" +  date ,
                                donedatetime=datetime.datetime.now())
              historysave.save()
              return Response(200)  
         else:
              return Response(serializeobj.errors) 
         
class Deleteresultview(APIView):
       def delete(self,request,id):
           obj= AddResult.objects.get(id=id)
           subject=request.data["subject"]
           name=request.data["name"]
           date=request.data["date"] 
           registernumber=request.data["regno"]
           userole=request.data["loggedInUserrole"]
           obj.delete()
           historysave=History(modelname=registernumber,
                                savedid=id,
                                operationdone='Delete Result',
                                donebyuser=request.data['loggedInUsername'],
                                donebyuserrole=request.data['loggedInUserrole'],
                                description= "student" +  "\t"  + name + "\t" + subject + "\t" "Result Has Been Deleted" + "\t" +  "in " + "\t" +  date ,
                                donedatetime=datetime.datetime.now())
           historysave.save()
           return Response(200)
class Addreaultindividualview(APIView):
       def get(self,request,id):
              obj= AddResult.objects.filter(id=id)
              serializeobj=AddResult_serializer(obj,many=True)
              return Response(serializeobj.data) 
# ................................................................................
             
class Applyleaveview(APIView):
       def get(self,request):
              obj= ApplyStaffLeave.objects.all()
              serializeobj=ApplyLeave_serializer(obj,many=True)
              return Response(serializeobj.data)  
       def post(self,request):
                                  
              serializeobj=ApplyLeave_serializer(data=request.data)
              
                 
              if serializeobj.is_valid():
                     device=serializeobj.save()
                     subject=request.data["subject"]
                     name=request.data["name"]
                     date=request.data["date"]
                     registernumber=request.data["regno"]
                     historysave=History(modelname= registernumber,
                                savedid=device.id,
                                operationdone='Staff Leave',
                                donebyuser=request.data['loggedInUsername'],
                                donebyuserrole=request.data['loggedInUserrole'],
                                description="Staff" + "\t" + name + "\t" + "Applyed  Leave" + "\t" + name + "\t"+"in" + date ,
                                donedatetime=datetime.datetime.now())
                     historysave.save()
                     return Response(200)
              else:
                     return Response(serializeobj.errors)
class UpdateStaff_Leave_view(APIView):
       def put(self,request,id):                     
          obj=ApplyStaffLeave.objects.get(id=id)
          subject=request.data["subject"]
          name=request.data["name"]
          date=request.data["date"] 
          registernumber=request.data["regno"]
          userole=request.data["loggedInUserrole"]
          serializeobj=ApplyLeave_serializer(obj,data=request.data) 
          if(serializeobj.is_valid()):
              device =serializeobj.save()
              historysave=History(modelname=registernumber,
                                savedid=device.id,
                                operationdone='Edit Staff Leave',
                                donebyuser=request.data['loggedInUsername'],
                                donebyuserrole=request.data['loggedInUserrole'],
                                description= "Staff" +  "\t"  + name + "\t" + subject + "\t" "Leave Has Been Edited" + "\t" +  "in " + "\t" +  date ,
                                donedatetime=datetime.datetime.now())
              historysave.save()
              return Response(200)  
          else:
              return Response(serializeobj.errors)               
              
class Delete_Staff_Leaveview(APIView):
       def delete(self,request,id):
           obj= ApplyStaffLeave.objects.get(id=id)
           obj= AddResult.objects.get(id=id)
           subject=request.data["subject"]
           name=request.data["name"]
           date=request.data["date"] 
           registernumber=request.data["regno"]
           userole=request.data["loggedInUserrole"]
           obj.delete()
           historysave=History(modelname=registernumber,
                                savedid=id,
                                operationdone='Delete Staff Leave',
                                donebyuser=request.data['loggedInUsername'],
                                donebyuserrole=request.data['loggedInUserrole'],
                                description= "Staff " +  "\t"  + name + "\t" + subject + "\t" "Leave Has Been Deleted" + "\t" +  "in " + "\t" +  date ,
                                donedatetime=datetime.datetime.now())
           historysave.save()
           return Response(200) 
# ................................................................................

class Apply_student_leaveview(APIView):
       def get(self,request):
              obj= Apply_Student_Leave.objects.all()
              serializeobj=Apply_Student_Leave_serializer(obj,many=True)
              return Response(serializeobj.data)  
       def post(self,request):
                                  
              serializeobj=Apply_Student_Leave_serializer(data=request.data)
              
                 
              if serializeobj.is_valid():
                     device=serializeobj.save()
                     subject=request.data["subject"]
                     name=request.data["name"]
                     date=request.data["date"]
                     registernumber=request.data["regno"]
                     historysave=History(modelname= registernumber,
                                savedid=device.id,
                                operationdone='Student Leave',
                                donebyuser=request.data['loggedInUsername'],
                                donebyuserrole=request.data['loggedInUserrole'],
                                description="Student" + "\t" + name + "\t" + "Applyed  Leave" + "\t" + name + "\t"+"in" + date ,
                                donedatetime=datetime.datetime.now())
                     historysave.save()
                     return Response(200)
              else:
                     return Response(serializeobj.errors)
class UpdateStudent_Leave_view(APIView):
       def put(self,request,id):                     
          obj=Apply_Student_Leave.objects.get(id=id)
          subject=request.data["subject"]
          name=request.data["name"]
          date=request.data["date"] 
          registernumber=request.data["regno"]
          userole=request.data["loggedInUserrole"]
          serializeobj=Apply_Student_Leave_serializer(obj,data=request.data) 
          if(serializeobj.is_valid()):
              device =serializeobj.save()
              historysave=History(modelname=registernumber,
                                savedid=device.id,
                                operationdone='Edit Student Leave',
                                donebyuser=request.data['loggedInUsername'],
                                donebyuserrole=request.data['loggedInUserrole'],
                                description= "Student" +  "\t"  + name + "\t" + subject + "\t" "Leave Has Been Edited" + "\t" +  "in " + "\t" +  date ,
                                donedatetime=datetime.datetime.now())
              historysave.save()
              return Response(200)  
          else:
              return Response(serializeobj.errors)               
              
class Delete_Student_Leaveview(APIView):
       def delete(self,request,id):
           obj= Apply_Student_Leave.objects.get(id=id)
           subject=request.data["subject"]
           name=request.data["name"]
           date=request.data["date"] 
           registernumber=request.data["regno"]
           userole=request.data["loggedInUserrole"]
           obj.delete()
           historysave=History(modelname=registernumber,
                                savedid=id,
                                operationdone='Delete Student Leave',
                                donebyuser=request.data['loggedInUsername'],
                                donebyuserrole=request.data['loggedInUserrole'],
                                description= "Student " +  "\t"  + name + "\t" + subject + "\t" "Leave Has Been Deleted" + "\t" +  "in " + "\t" +  date ,
                                donedatetime=datetime.datetime.now())
           historysave.save()
           return Response(200)                                 