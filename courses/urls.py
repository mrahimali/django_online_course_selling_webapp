from django.urls import path
from courses.views.Auth import signup, login
from courses.views import home, CourseDetail

urlpatterns = [
    path('', home, name='home'),
    path('course/<str:slug>', CourseDetail , name='coursepage'),
    path('signup/', signup , name='signup'),
    path('login/', login, name='login')
]