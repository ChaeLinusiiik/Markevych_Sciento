from django.urls import path

from . import views

urlpatterns=[
    path('', views.home, name = 'home' ),
    path('schedule/', views.schedule, name ='schedule'),
    path('courses/', views.base_courses, name ='base_courses')
]