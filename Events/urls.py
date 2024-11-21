from django.urls import path
from .import views
from django.contrib import admin
from . import views as user_views
from django.contrib.auth import views as auth_views
app_name = 'events'

urlpatterns=[
    path('', views.home, name='index'),
    path('add-event/', views.add_event, name='add_event'),
    path('events/', user_views.events, name='all-events'),
    path('event/delete/', views.delete_event, name='delete-event'),
    path('update-event/', user_views.update_event, name='upd-event'),
    path('register/', user_views.register_event, name='user-registration'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='user-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='user-logout'),
    path('events_today/', user_views.events_today, name='events-today'),
]