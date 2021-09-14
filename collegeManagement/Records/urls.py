from django.urls import path

from . import views

urlpatterns=[
    path('addStu/',views.StudentRegisterView,name='addstudent'),
    path('ho/',views.homeView,name='Home'),
    path('add-dep/',views.DepartmentRegisterView,name='Add-dep'),
    path('Show-Stu/',views.ShowStudentView,name='Showstudent'),
    path('Show-Lec/',views.ShowLecturerView,name='Showlecture'),
    path('add-lec/',views.AddLecturerView,name='Addlecture'),
    path('updatestu/<int:update>',views.UpdateStudentView,name='Updatestudent'),
    path('updatelecturer/<int:update>',views.UpdateLecturerView,name='Updatelecture'),
    path('deletestu/<int:delete>',views.DeleteStudentView,name='Deletestudent'),
    path('deletelecturer/<int:delete>',views.DeleteLecturerView,name='Deletelecture'),
    path('search/',views.Search_view,name='Search'),


    
    
]