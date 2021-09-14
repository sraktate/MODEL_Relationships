
from django.contrib import messages
from .forms import DepartmentForm, LectureForm, StudentForm
from .models import Department, Lecture, Student
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

# Create your views here.

def StudentRegisterView(request):
    form=StudentForm()
    if request.method == 'POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addstudent')
    template_name='Record_tem/AddStudent.html'
    context={'form':form}
    return render(request,template_name,context)

@login_required(login_url='login')
def ShowStudentView(request):
    stu=Student.objects.all()
    template_name='Record_tem/showStudent.html'
    context={'stu':stu}
    return render(request,template_name,context)

def homeView(request):
    template_name = "Record_tem/Home.html"
    context ={}
    return render(request,template_name,context)

@login_required(login_url='login')
def DepartmentRegisterView(request):
    form = DepartmentForm()
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            dep = request.POST.get('DName')
            dep1 = Department.objects.filter(DName=dep).first()
            if dep1 is not None:
                messages.error(request,'Department is already present')
                return redirect('Add-dep')
            form.save()
            return redirect('Add-dep')
    template_name = 'Record_tem/AddDepartment.html'
    context = {'form':form}
    return render(request,template_name,context)

@login_required(login_url='login')
def AddLecturerView(request):
        form=LectureForm()
        if request.method == 'POST':
            form=LectureForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('Addlecture')
        template_name='Record_tem/AddLecture.html'
        context={'form':form}
        return render(request,template_name,context)

@login_required(login_url='login')
def ShowLecturerView(request):
    ltu=Lecture.objects.all()
    template_name='Record_tem/ShowLecture.html'
    context={'stu':ltu}
    return render(request,template_name,context)

def UpdateStudentView(request,update):
    stu=Student.objects.get(id=update)
    form=StudentForm(instance=stu)
    if request.method == 'POST':
        form=StudentForm(request.POST,instance=stu)
        if form.is_valid():
            form.save()
            return redirect('Showstudent')
    template_name='Record_tem/AddStudent.html'
    context={'form':form}
    return render(request,template_name,context)

def UpdateLecturerView(request,update):
    lec=Lecture.objects.get(id=update)
    form=LectureForm(instance=lec)
    if request.method == 'POST':
        form=LectureForm(request.POST,instance=lec)
        if form.is_valid():
            form.save()
            return redirect('Showlecture')
    template_name='Record_tem/ShowLecture.html'
    context={'form':form}
    return render(request,template_name,context)

def DeleteStudentView(request,delete):
    stu=Student.objects.get(id=delete)
    stu.delete()
    return redirect('Showstudent')

def DeleteLecturerView(request,delete):
    stu=Lecture.objects.get(id=delete)
    stu.delete()
    return redirect('Showlecture')

@login_required(login_url='login')
def Searchview(request):
    if request.method == 'POST':
        radio=request.POST.get('dep')
        if radio == 'Department':
            search=request.POST.get('search')
            dep_obj=Department.objects.get(DName=search)
            dep_id=dep_obj.id
            lecresult=Lecture.objects.filter(department=dep_id)
            sturesult=Student.objects.filter(department_id=dep_id)
            template_name='Record_tem/search.html'
            context={'lecresult':lecresult,'sturesult':sturesult}
            return render(request,template_name,context)
        elif radio == 'Student':
            search=request.POST.get('search')
            sturesult=Student.objects.filter(SName=search)
            template_name='Record_tem/search.html'
            context={'sturesult':sturesult}
            return render(request,template_name,context)

        elif radio == 'Lecture':
            search=request.POST.get('search')
            lecresult=Lecture.objects.filter(LName=search)
            template_name='Record_tem/search.html'
            context={'lecresult':lecresult}
            return render(request,template_name,context)
    template_name='Record_tem/search.html'
    context={}
    return render(request,template_name,context)