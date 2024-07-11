from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin1030/', admin.site.urls),
    path('', include('posts.urls')),
]
