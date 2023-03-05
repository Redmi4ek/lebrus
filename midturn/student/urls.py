from django.urls import path
from student import views

urlpatterns = [
    path('api/students', views.students_handler),
    path('api/students/<int:pk>', views.student_handler)

]