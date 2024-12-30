from django.shortcuts import render
from .models import Student, Tutor


def users(request):
    lastest_tutors = Tutor.objects.order_by('hourly_rate')
    return render(request, 'users/list.html', {"lastest_tutors":lastest_tutors})

