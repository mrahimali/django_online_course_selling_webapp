from django.shortcuts import redirect, render
from courses.models import Course


def CreateOrder(request, slug):
    course = Course.objects.get(slug = slug)

    if not request.user.is_authenticated:
        return redirect('login')
    
    context = {
        'course':course,
    }

    return render(request, 'courses/checkout.html', context)

