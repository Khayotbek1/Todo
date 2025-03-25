
from django.contrib import admin
from django.urls import path

from main.views import students_view, home_view, task_view, not_done, course_3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('students/', students_view,  name = 'students'),
    path('tasks/', task_view, name='tasks'),
    path('tasks/not_done/', not_done, name='not_done'),
    path('students/course_3/', course_3, name='course_3')
]
