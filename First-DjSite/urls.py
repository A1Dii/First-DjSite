from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('First-DjSite.apps.site.urls')),
    path('admin/', admin.site.urls),
]
