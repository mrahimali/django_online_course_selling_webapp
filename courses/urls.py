from django.urls import path
from courses.views import home, CourseDetail

urlpatterns = [
    path('', home, name='home'),
    path('course/<str:slug>', CourseDetail , name='coursepage')
]