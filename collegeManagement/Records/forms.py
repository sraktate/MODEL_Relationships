from django import forms

from .models import Student,Department,Lecture


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = '__all__'
        widgets ={
            'department':forms.CheckboxSelectMultiple()
        }