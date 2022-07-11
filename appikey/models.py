from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=120)
    amount = models.IntegerField()

    def __str__(self):
        return self.name

class School(models.Model):
    name = models.CharField(max_length=80)
    clg = models.CharField(max_length=100)
    city = models.CharField(max_length=90)
    salary = models.IntegerField()

    def __str__(self):
        return self.clg

class Exam(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    salary = models.IntegerField()
    Clg = models.CharField(max_length=100)

