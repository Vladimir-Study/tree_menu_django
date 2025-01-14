"""
URL configuration for tree_menu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from tree_main_menu.views import index

urlpatterns = [
    path('', index, name='main'),
    path('main_1/', index, name='main_1'),
    path('main_2/', index, name='main_2'),
    path('main_1_1/', index, name='main_1_1'),
    path('main_1_2/', index, name='main_1_2'),
    path('main_2_1/', index, name='main_2_1'),
    path('main_2_2/', index, name='main_2_2'),
    path('admin/', admin.site.urls),
]
