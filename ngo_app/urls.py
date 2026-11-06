from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('donate/', views.donate, name='donate'),
    path('volunteer/', views.volunteer, name='volunteer'),
    path('contact/', views.contact, name='contact'),
   
   # Authentication
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
