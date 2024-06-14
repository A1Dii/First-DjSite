from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('First-DjSite.pages.apps.Site.urls')),
    path('admin/', admin.site.urls),
]
