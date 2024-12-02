from django.contrib import admin
from .models import Student, Course

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'email', 'gender')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'max_student')
