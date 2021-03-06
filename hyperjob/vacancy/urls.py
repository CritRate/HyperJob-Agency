from django.urls import path
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    path('vacancies/', views.all_vacancies, name='all_vacancies'),
    path('vacancy/new', RedirectView.as_view(pattern_name='new_vacancy'), name='redirect_vacancy'),
    path('vacancy/new/', views.new_vacancy, name='new_vacancy'),
]
