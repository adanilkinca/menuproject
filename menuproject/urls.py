"""
URL configuration for menuproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from menuapp.views import demo_form_view
# from menuapp.views import home, register, login
from menuapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo-form/', demo_form_view, name='demo-form'),
    # path('home/', views.form_view),
    path('', include('menuapp.urls')),
    # path('about/', views.about, name='about'),
    # path('menuapp/home/', home, name='home'),
    # path('menuapp/register/', register, name='register'),
    # path('menuapp/login/', login, name='login'),  
]
