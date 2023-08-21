from django.urls import path
from . import views

urlpatterns = [
    # path('menu/', views.menu), -- commented in views.py
    path('menu_card/', views.menu_by_id),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    # path('register/', views.register, name='register'),  
    # path('login/', views.login, name='login'),    
]