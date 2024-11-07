from rest_framework import serializers
from Staffapp .models import Attendance_Maths,Attendance_Account,Attendance_Che,Attendance_Eng,Attendance_Malay,Attendance_History,Attendance_Phy,All_Attendance,AddResult,ApplyStaffLeave,Apply_Student_Leave
class Attendancemaths_serializer(serializers.ModelSerializer):
                    class Meta:
                       model=Attendance_Maths
                       fields="__all__"
                       
class Attendanceeng_serializer(serializers.ModelSerializer):
                    class Meta:
                       model=Attendance_Eng
                       fields="__all__"
                       
class Attendancemal_serializer(serializers.ModelSerializer):
                    class Meta:
                       model=Attendance_Malay
                       fields="__all__"
                       
class Attendancephy_serializer(serializers.ModelSerializer):
                    class Meta:
                       model=Attendance_Phy
                       fields="__all__"
                       
class Attendancechy_serializer(serializers.ModelSerializer):
               class Meta:
                       model=Attendance_Che
                       fields="__all__"       
                       
class Attendanceaccount_serializer(serializers.ModelSerializer):
                    class Meta:
                       model=Attendance_Account
                       fields="__all__"
                       
class Attendancehistory_serializer(serializers.ModelSerializer):
                    class Meta:
                       model=Attendance_History
                       fields="__all__"           
                       
class All_Attendance_serializer(serializers.ModelSerializer):
                    class Meta:
                       model=All_Attendance
                       fields="__all__"    
                       
class AddResult_serializer(serializers.ModelSerializer):
                    class Meta:
                       model=AddResult
                       fields="__all__"   
class ApplyLeave_serializer(serializers.ModelSerializer):
                    class Meta:
                       model=ApplyStaffLeave
                       fields="__all__" 
                       
class Apply_Student_Leave_serializer(serializers.ModelSerializer):
                    class Meta:
                       model=Apply_Student_Leave
                       fields="__all__"                                                                                                                                                                                                                             