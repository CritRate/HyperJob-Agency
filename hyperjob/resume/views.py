from django.shortcuts import render, redirect, reverse, HttpResponse
from django.core.exceptions import PermissionDenied
from .models import Resume
from .forms import ResumeForm


# Create your views here.

def all_resumes(request):
    data = Resume.objects.all()
    return render(request, 'resume/all_resumes.html', {'resumes': data})


def new_resume(request):
    if not request.user.is_authenticated or request.user.is_staff:
        return HttpResponse(status=403)
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            Resume.objects.create(description=form.cleaned_data['description'], author=request.user)
    return redirect(reverse('home'))
