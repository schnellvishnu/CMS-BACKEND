from django.urls import path
from Staffapp import views
urlpatterns = [
    path("attendance_maths/",views.Attendance_MATHS_get.as_view()),  
    path("deleteattendance_maths/<id>",views.DeleteAttendance_MATHS_view.as_view()),
    
    path("attendance_eng/",views.Attendance_ENG_get.as_view()),  
    path("deleteattendance_eng/<id>",views.DeleteAttendance_ENG_view.as_view()),               
    
    path("attendance_account/",views.Attendance_ACCOUNT_get.as_view()),  
    path("deleteattendance_account/<id>",views.DeleteAttendance_ACCOUNT_view.as_view()),               
    
    path("attendance_che/",views.Attendance_CHE_get.as_view()),  
    path("deleteattendance_che/<id>",views.DeleteAttendance_CHE_view.as_view()),               
    
    path("attendance_mal/",views.Attendance_MALAYALAM_get.as_view()),  
    path("deleteattendance_mal/<id>",views.DeleteAttendance_MALAYALAM_view.as_view()),               
    
    path("attendance_phy/",views.Attendance_PHY_get.as_view()),  
    path("deleteattendance_phy/<id>",views.DeleteAttendance_PHY_view.as_view()),               
    
    path("attendance_his/",views.Attendance_HISTORY_get.as_view()),  
    path("deleteattendance_his/<id>",views.DeleteAttendance_HISTORY_view.as_view()),   
    
    path("all_attendance/",views.All_Attendance_get.as_view()),  
    path("delete_all_attendance/<id>",views.Delete_All_Attendance__view.as_view()), 
    
    path("attendance_view/",views.Attendance_viewpage_post.as_view()),
    path("attendance_individual/<id>",views.Attendanceindividulaview.as_view()), 
    path("update_attendance/<id>",views.Update_Attendance.as_view()), 
    
    path("addresult/",views.Addreaultview.as_view()),
    path("updateresult/<id>",views.Updateresultview.as_view()),
    path("delete_result/<id>",views.Deleteresultview.as_view()),
    path("result_individual/<id>/",views.Addreaultindividualview.as_view()),
    
    path("staff_leave/",views.Applyleaveview.as_view()),
    path("update_staff_leave/<id>",views.UpdateStaff_Leave_view.as_view()),
    path("delete_staff_leave/<id>",views.Delete_Staff_Leaveview.as_view()),
    
    path("student_leave/",views.Apply_student_leaveview.as_view()),
    path("update_student_leave/<id>",views.UpdateStudent_Leave_view.as_view()),
    path("delete_student_leave/<id>",views.Delete_Student_Leaveview.as_view()),
      
       
                   
    
                         
]