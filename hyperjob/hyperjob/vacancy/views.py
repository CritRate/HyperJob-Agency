from django.shortcuts import render, redirect, reverse
from django.core.exceptions import PermissionDenied
from .models import Vacancy
from .forms import VacancyForm


# Create your views here.

def all_vacancies(request):
    data = Vacancy.objects.all()
    return render(request, 'vacancy/all_vacancies.html', {'vacancies': data})


def new_vacancy(request):
    if request.method == 'POST':
        form = VacancyForm(request.POST)
        if request.user.is_authenticated and request.user.is_staff:
            if form.is_valid():
                Vacancy.objects.create(description=form.cleaned_data['description'], author=request.user)
        else:
            raise PermissionDenied()
    else:
        form = VacancyForm()
        return render(request, 'vacancy/new_vacancy.html', {'form': form})
    return redirect(reverse('home'))
