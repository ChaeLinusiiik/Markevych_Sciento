from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),          # URL-адреси для користувачів
    path('home/', include('core.urls')),
    path('courses/', include('courses.urls')),      # URL-адреси для курсів
    path('sessions/', include('base_sessions.urls')),    # URL-адреси для сесій
    path('payments/', include('payments.urls')),    # URL-адреси для платежів
]
