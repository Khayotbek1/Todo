from django.contrib import admin
from django.urls import path
from main.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('students/', students_view,  name = 'students'),
    path('tasks/', task_view, name='tasks'),
    path('tasks/create-task/', create_task, name='create-task'),
    path('tasks/not_done/', not_done, name='not_done'),
    path('tasks/<int:pk>/delete-confirm/', task_delete_confirm, name='delete-confirm'),
    path('tasks/<int:pk>/delete/', task_delete, name='task-delete'),
    path('students/course_3/', course_3, name='course_3'),
    path('students/age_20/', age_20, name='age_20'),
]
