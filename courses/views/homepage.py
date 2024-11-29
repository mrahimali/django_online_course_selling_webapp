from django.shortcuts import render, HttpResponse
from courses.models import Course

def home(request):
    courses=Course.objects.all()
    print(courses)
    return render(request, 'courses/home.html', context={'courses':courses})