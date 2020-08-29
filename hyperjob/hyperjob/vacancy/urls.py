from django.urls import path

from . import views

urlpatterns = [
    path('vacancies/', views.all_vacancies, name='all_vacancies'),
    path('vacancy/new/', views.new_vacancy, name='new_vacancy'),
]
