from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse

#@login_required
def home(request):
    return render(request, 'home/home.html')

def schedule(request):
    return render(request, 'schedule/schedule.html')

def base_courses(request):
    return render(request, 'courses/base_courses.html')