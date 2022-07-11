from django.contrib import admin
from .models import Student, School , Exam

# Register your models here.

@admin.register(Student)
class AdminStudent(admin.ModelAdmin):
    list_display = ['id', 'name', 'city', 'amount']

@admin.register(School)
class AdminSchool(admin.ModelAdmin):
    list_display = ['id','name','clg','city','salary']


@admin.register(Exam)
class AdminExamcen(admin.ModelAdmin):
    list_display = ['salary','Clg','student']