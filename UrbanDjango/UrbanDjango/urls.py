"""
URL configuration for UrbanDjango project.

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
from django.urls import path
from task2.views import func_templates, Class_template
from task3.views import func_platform, func_games, func_cart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', func_templates),
    path('class/', Class_template.as_view()),
    path('platform', func_platform),
    path('platform/games', func_games),
    path('platform/cart', func_cart),
]