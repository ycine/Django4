"""Django4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path, include
from django_4.views import strona_glowna, strona_glowna2
from rest_framework import routers 
from django_4.views import TechnologieViewSet, TechnologieViewSet2


router = routers.DefaultRouter()
router.register('technologie', TechnologieViewSet2)
# router.register('technologie', TechnologieViewSet)




urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('django_4/', TechnologieViewSet.as_view(), name='django_4'),
    
    path('', strona_glowna),  
    path('2', strona_glowna2), 
    path('technologie/', include(router.urls)),   
    path('3', TechnologieViewSet.as_view()), 
]
