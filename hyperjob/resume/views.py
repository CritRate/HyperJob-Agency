from django.shortcuts import render, redirect, reverse
from django.core.exceptions import PermissionDenied
from .models import Resume
from .forms import ResumeForm


# Create your views here.

def all_resumes(request):
    data = Resume.objects.all()
    return render(request, 'resume/all_resumes.html', {'resumes': data})


def new_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if request.user.is_authenticated and not request.user.is_staff:
            if form.is_valid():
                Resume.objects.create(description=form.cleaned_data['description'], author=request.user)
        else:
            raise PermissionDenied()
    else:
        form = ResumeForm()
        return render(request, 'resume/new_resume.html', {'form': form})
    return redirect(reverse('home'))
