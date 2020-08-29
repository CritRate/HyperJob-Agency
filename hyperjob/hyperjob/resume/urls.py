from django.urls import path
from . import views

urlpatterns = [
    path('resumes/', views.all_resumes, name='all_resumes'),
    path('resume/new/', views.new_resume, name='new_resume'),
]
