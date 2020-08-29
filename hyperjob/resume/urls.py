from django.urls import path
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    path('resumes/', views.all_resumes, name='all_resumes'),
    path('resume/new/', RedirectView.as_view(pattern_name='new_resume'), name='redirect_resume'),
    path('resume/new', views.new_resume, name='new_resume'),
]
