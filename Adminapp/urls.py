from django.urls import path
from Adminapp import views
urlpatterns = [
   
   path("coursedetail/",views.CourseView.as_view()),
   path("coursedetailind/<id>",views.CourseViewIndividual.as_view()),
   path("updatecourse/<id>",views.UpdateCourse.as_view()),
   path("deletecourse/<id>",views.DeleteCourse.as_view()),
   
   path("staffdetail/",views.Staffgetview.as_view()), 
   path("updatestaff/<id>",views.Updatestaff.as_view()),
   path("deletestaff/<id>",views.Deletestaff.as_view()),
   path("staffindividual/<id>",views.Staffindividual.as_view()),
   
   path("studentdetail/",views.Studentgetview.as_view()), 
   path("updatestudent/<id>",views.Updatestudent.as_view()),
   path("deletestudent/<id>",views.Deletestudent.as_view()),
   path("studentindividual/<id>",views.StudentgetIndividual.as_view()),
   path("student_registerno/<id>",views.Studentget_Data_Registernumber.as_view()),
   path("student_course/<id>/",views.Studentget_Data_Cousebased.as_view()),
   
   path("subjectdetail/",views.Subjectview.as_view()), 
   path("updatesubject/<id>",views.Updatesubject.as_view()),
   path("deletesubject/<id>",views.Deletesubjet.as_view()),
   path("subjectindividual/<id>",views.Subjectindividual.as_view()),
   
   path("student_notification/",views.NotificationstudentView.as_view()),
   path("update_student_notification/<id>",views.Update_Student_Notif.as_view()), 
   path("delete_student_notification/<id>",views.DeleteStudentnotification.as_view()),
   path("student_notification_individual/<id>",views.NotifictionStudentIndividual.as_view()),
   
   path("staff_notification/",views.Notification_StaffView.as_view()), 
   path("update_staff_notification/<id>",views.Update_Staff_Notif.as_view()),
   path("delete_staff_notification/<id>",views.Delete_Staffnotification.as_view()),
   path("staff_notification_individual/<id>/",views.NotifictionStaff_Individual.as_view()),
   
   path("history/",views.History_View.as_view()), 
   path("delete_history/<id>",views.Delete_History.as_view()),
   
   ]