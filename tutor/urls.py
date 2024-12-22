from django.urls import path
from django.shortcuts import redirect
from . import views

app_name = 'tutor'

urlpatterns = [
    # path('', lambda request: redirect('home:index'), name='home'),  # Redirect to the home app's index
    path('', views.mentor_list, name='mentor_list'),  # Point `/tutor` to `/mentors`
    path('mentor/<int:mentor_id>/', views.mentor_profile, name='mentor_profile'),
    path('send_request/<int:mentor_id>/', views.send_request, name='send_request'),
]
