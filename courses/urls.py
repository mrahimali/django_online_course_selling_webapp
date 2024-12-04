from django.urls import path
from courses.views.Auth import SignUp, LoginView, SignOut
from courses.views import home, CourseDetail, CreateOrder

urlpatterns = [
    path('', home, name='home'),
    path('course/<str:slug>', CourseDetail , name='coursepage'),
    
    path('signup/', SignUp.as_view() , name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', SignOut, name='signout'),
    path('checkout/<str:slug>', CreateOrder, name='checkout'),
]