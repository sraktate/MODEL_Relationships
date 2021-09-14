from .models import Department, Lecture, Student
from django.contrib import admin

# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id','DName','DIntake']
admin.site.register(Department,DepartmentAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display=['id','SName','Roll_no','Marks','SAddress','department']
admin.site.register(Student,StudentAdmin)

class LectureAdmin(admin.ModelAdmin):
    list_display=['id','LName','Sal','Lsub','written_by']
admin.site.register(Lecture,LectureAdmin)