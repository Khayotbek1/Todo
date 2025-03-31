from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template.context_processors import request
from django.template.loader import render_to_string

from .models import *

def home_view(request):
    home = Student.objects.all()

    return render(request, 'home.html', {'home': home})

def students_view(request):
    students = Student.objects.all()
    context = {
        'students': students
    }

    return render(request, 'students.html', context)

def task_view(request):
    task = Task.objects.all()
    context = {
        'tasks': task
    }
    return render(request, 'tasks.html', context)

def create_task(request):
    if request.method == 'POST':
        Task.objects.create(
            name = request.POST.get('vazifa'),
            student = Student.objects.get(id = request.POST.get('student_id')),
            date = request.POST.get('sana'),
            desc = request.POST.get('batafsil'),
        )

        return redirect('tasks')

    student = Student.objects.all()
    context = {
        'students': student,
    }

    return render(request, 'create_task.html', context)

def task_delete_confirm(request, pk):
    task = Task.objects.get(id = pk)
    context = {
        'task' : task,
    }
    return render(request, 'task-delete-confirm.html', context)

def task_delete(request, pk):
    task = Task.objects.get(id = pk)
    task.delete()
    return redirect('tasks')

def not_done(request):
    task = Task.objects.filter(done = False)
    context = {
        'tasks': task
    }
    return render(request, 'not_done.html', context)

def course_3(request):
    course = Student.objects.filter(course__gte = 3)
    context = {
        'courses': course,
    }
    return render(request, 'course3.html', context )

def age_20(request):
    age = Student.objects.filter(age__gt = 20)
    context = {
        'ages': age
    }
    return render(request, 'age_20.html', context)

def graduate_task(request):
    graduates = Student.objects.filter(course__gte=5)
    tasks = Task.objects.filter(student__course__gte=5).order_by('name')

    context = {
        'graduates': graduates,
        'tasks': tasks,
    }
    return render(request, 'graduate_task.html', context)
