"""
URL configuration for education project.

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
from anynomous import views as anoviews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('index', anoviews.index),

    path('header',anoviews.header),
    
    path('footer',anoviews.footer),

    path('base',anoviews.base),

    path('',anoviews.homepage),

    path('features',anoviews.features),

    path('experties',anoviews.experties),

    path('contactus',anoviews.contactus),
    
    path('gallery', anoviews.gallery),
    
    path('login',anoviews .login),

    path('signup',anoviews.signup),
    
    path('testprops',anoviews.testprops),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
