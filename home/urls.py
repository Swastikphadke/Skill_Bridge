
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name='index'),
    path('quiz/',views.quiz,name='quiz'),
    # path('resource/',views.resource,name='resources'),
    # path('query/',views.query,name='query'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login_view,name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('modify_profile/', views.modify_profile, name='modify_profile'),
    path('accept_request/<int:request_id>/', views.accept_request, name='accept_request'),
    path('reject_request/<int:request_id>/', views.reject_request, name='reject_request'),
    path('project_collab/', views.project_collaboration, name='project_collab'),
]
