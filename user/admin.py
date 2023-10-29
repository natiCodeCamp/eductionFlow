from django.contrib import admin
from schedules.models import Teacher,Student

# Register your models here.
class TeacherAdmin(admin.ModelAdmin):
    list_display = ["subject"]
class StudentAdmin(admin.ModelAdmin):
    list_display =["grade"]
admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Student,StudentAdmin)