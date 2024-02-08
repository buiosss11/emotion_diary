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
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list,name="post-list"),
    path('new/', views.post_create,name="post-create"),
    path('<int:post_id>', views.post_detail,name="post-detail"),
    # path('<int:post_id>/edit', views.post_edit,name="posts-edit"),
    path('<int:post_id>/delete', views.post_delete,name="post-delete"),
]
