from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.shortcuts import render
from django.urls import reverse_lazy

from resume.models import Resume
from vacancy.models import Vacancy
from resume.forms import ResumeForm
from vacancy.forms import VacancyForm


def index(request):
    return render(request, 'index.html')


class MySignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class MyLogInView(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    template_name = 'login.html'


def home(request):
    resumes = Resume.objects.all()
    vacancies = Vacancy.objects.all()
    if request.user.is_staff:
        form = VacancyForm()
    else:
        form = ResumeForm()
    return render(request, 'home.html', {
        'resumes': resumes,
        'vacancies': vacancies,
        'form': form
    })
