"""
URL configuration for emotion_diary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('login/', auth_views.LoginView.as_view(),name="user-login"),
    path('login/', views.user_login ,name="user-login"),
    path('logout/', views.user_logout, name="user-logout"),
    path('new/', views.user_create, name="user-create"),
    path('pw_edit/', views.user_pw_edit, name="user-pw-change"),
    path('edit/<int:user_id>/', views.user_edit, name="user-edit"),
]
