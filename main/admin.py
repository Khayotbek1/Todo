from django.contrib import admin

from .models import *


class TaskInline(admin.StackedInline):
    model =Task
    extra = 1



class StudentAdmin(admin.ModelAdmin):
        list_display = ('name', 'course', 'number')
        search_fields = ('name', 'number')
        inlines = (TaskInline,)

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'student', 'done')
    search_fields = ('name', 'student', 'done')



admin.site.register(Student, StudentAdmin)
admin.site.register(Task, TaskAdmin)