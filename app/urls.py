"""
URL configuration for authentication project.

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
from app import views

urlpatterns = [
    path('',views.SignupPage,name="signup"),
    path('home/',views.HomePage,name="home"),
    path('login/',views.LoginPage,name="login"),
    path('logout/',views.Logout,name="logout"),
    path('create/',views.CreatePage,name="create"),
    path('view/',views.ViewPage,name="view"),
    path('view/update/<int:id>',views.Update,name="update"),
    path('update/uprec/<int:id>',views.Uprec,name="uprec"),
    path('view/remove/<int:id>',views.Remove,name="remove"),
]