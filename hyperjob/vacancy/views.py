from django.shortcuts import render, redirect, reverse, HttpResponse
from django.core.exceptions import PermissionDenied
from .models import Vacancy
from .forms import VacancyForm


# Create your views here.

def all_vacancies(request):
    data = Vacancy.objects.all()
    return render(request, 'vacancy/all_vacancies.html', {'vacancies': data})


def new_vacancy(request):
    if not request.user.is_authenticated or not request.user.is_staff:
        return HttpResponse(status=403)
    if request.method == 'POST':
        form = VacancyForm(request.POST)
        if form.is_valid():
            Vacancy.objects.create(description=form.cleaned_data['description'], author=request.user)
    return redirect(reverse('home'))
