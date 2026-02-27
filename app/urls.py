from django.urls import path
from .views import register_student

urlpatterns = [
    path('', register_student, name='register_student'),
]