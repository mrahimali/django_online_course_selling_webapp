from django.shortcuts import render, HttpResponse, redirect
# from django.contrib.auth.forms import UserCreationForm
from courses.forms import RegistrationForm, LoginForm
from django.views import View
from django.contrib.auth import logout

class SignUp(View):
    def get(self, request):
        form = RegistrationForm()
        return render( request, 'courses/signup.html', {'form':form})
    
    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            if user is not None:
                return redirect('login')
        return render( request, 'courses/signup.html', {'form':form})



# def SignUp(request):
#     if request.method == 'GET':
#         # form = UserCreationForm()
#         form = RegistrationForm()
#         return render( request, 'courses/signup.html', {'form':form})
#     form = RegistrationForm(request.POST)
#     if form.is_valid():
#         user=form.save()
#     return render( request, 'courses/signup.html', {'form':form})


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        context={
            'form':form
        }
        return render(request, 'courses/login.html', context)
    
    def post(self, request):
        form = LoginForm(request, data = request.POST)
        context={
            'form':form
        }
        if form.is_valid():
            return redirect('home')
        return render(request, 'courses/login.html', context)

# def login(request):
#     return render( request, 'courses/login.html')


def SignOut(request):
    logout(request)
    return redirect('home')

