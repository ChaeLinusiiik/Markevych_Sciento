from django.urls import path

from . import views

urlpatterns=[
    path('', views.base_sessions, name = 'base_sessions' )
]