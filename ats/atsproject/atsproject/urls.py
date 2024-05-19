"""
URL configuration for atsproject project.

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
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('atsapp.urls')),
    path('home/', include('atsapp.urls')),
    path('sitterstatus/', include('atsapp.urls')),
    path('babycheckin/', include('atsapp.urls')),
    path('babycheckout/', include('atsapp.urls')),
    path('babylist/', include('atsapp.urls')),
    path('babyregistration/', include('atsapp.urls')),
    path('bcheckinrecord/', include('atsapp.urls')),
    path('bcheckoutrecord/', include('atsapp.urls')),
    path('editinfo/', include('atsapp.urls')),
    path('financereport/', include('atsapp.urls')),
    path('inventory/', include('atsapp.urls')),
    path('login/', include('django.contrib.auth.urls')),
    path('login/', include('atsapp.urls')),
    path('purchaseorder/', include('atsapp.urls')),
    path('salesorder/', include('atsapp.urls')),
    path('salesreport/', include('atsapp.urls')),
    path('sitterlist/', include('atsapp.urls')),
    path('sitterregistration/', include('atsapp.urls')),
    path('dashboard/', include('atsapp.urls')),
    path('search/', include('atsapp.urls')),
   
]
