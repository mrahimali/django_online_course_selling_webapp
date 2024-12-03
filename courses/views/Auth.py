from django.shortcuts import render, HttpResponse
# from django.contrib.auth.forms import UserCreationForm
from courses.forms import RegistrationForm


def signup(request):
    if request.method == 'GET':
        # form = UserCreationForm()
        form = RegistrationForm()
        return render( request, 'courses/signup.html', {'form':form})
    form = RegistrationForm(request.POST)
    if form.is_valid():
        user=form.save()
    return render( request, 'courses/signup.html', {'form':form})


def login(request):
    return render( request, 'courses/login.html')

