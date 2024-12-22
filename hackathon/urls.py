
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('tutor/', include('tutor.urls')),
    path('resources/', include('uploads.urls')),
    path('query/', include('qa.urls')),
]
