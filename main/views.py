from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
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

def not_done(request):
    task = Task.objects.filter(done = False)
    context = {
        'tasks': task
    }
    return render(request, 'not_done.html', context)

def course_3(request):
    course = Student.objects.filter(course__gte = 3)
    context = {
        'course': course,
    }
    return render(request, 'course3.html', context )
