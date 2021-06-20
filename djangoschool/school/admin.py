from .models import AllStudent, ExamScore
from django.contrib import admin

# Register your models here.
class StudentScore(admin.ModelAdmin):
    list_display = ['student_name', 'subject', 'score']
    list_filter = ['subject']

admin.site.register(ExamScore, StudentScore)

class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'level', 'student_name', 'student_tel']
    list_filter = ['level']
    list_editable = ['student_tel']

admin.site.register(AllStudent, StudentAdmin)