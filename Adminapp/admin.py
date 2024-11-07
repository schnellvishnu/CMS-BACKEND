from django.contrib import admin
from Adminapp.models import Coursemodel,Staffmodel,Studentmodel,Subject_model,Notifiction_Student,Notifiction_Staff,History
# Register your models here.
admin.site.register(Coursemodel)
admin.site.register(Staffmodel)
admin.site.register(Studentmodel)
admin.site.register(Subject_model)
admin.site.register(Notifiction_Student)
admin.site.register(Notifiction_Staff)
admin.site.register(History)