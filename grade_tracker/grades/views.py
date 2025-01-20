from django.shortcuts import render, redirect
from .models import Grade
from .forms import GradeForm
from django.db.models import Avg  # Import Avg from django.db.models

def home(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = GradeForm()

    grades = Grade.objects.all()
    average = grades.aggregate(Avg('grade'))['grade__avg'] or 0  # Use Avg here

    return render(request, 'grades/home.html', {'form': form, 'grades': grades, 'average': average})
