from django.db import models

# Create your models here.


class Department(models.Model):
    DName = models.CharField(max_length=400)
    DIntake = models.IntegerField()

    def __str__(self):
        return self.DName

class Student(models.Model):
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    Roll_no = models.IntegerField()
    SName = models.CharField(max_length=30)
    Marks = models.FloatField()
    SAddress = models.CharField(max_length=100)
    def __str__(self) :
        return self.SName

class Lecture(models.Model):
    department = models.ManyToManyField(Department)
    LName = models.CharField(max_length=30)
    Sal = models.FloatField()
    Lsub = models.CharField(max_length=30)

    def written_by(self):
        return ",".join([str(p) for p in self.department])

    def __str__(self) :
        return self.LName
