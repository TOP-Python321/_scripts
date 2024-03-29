"""
URL configuration for library project.

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

# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path

from catalog import views


urlpatterns = [
    # http://127.0.0.1:8000/admin/
    # http://127.0.0.1:8000/admin/login
    # http://127.0.0.1:8000/admin/password_change
    path('admin', admin.site.urls), 
    
    # http://127.0.0.1:8000/login
    path('login', LoginView.as_view()),
    # http://127.0.0.1:8000/logout
    path('logout', views.logout),
    
    # http://127.0.0.1:8000/
    path('', views.hello),
    
    # http://127.0.0.1:8000/catalog
    path('catalog', views.catalog),
    
    # http://127.0.0.1:8000/publishers/ast
    # http://127.0.0.1:8000/publishers/azbuka
    # path('publishers/<str:publisher>', views.publisher),
    path('publishers/<slug>', views.Publisher.as_view()),
    
    path('test', views.test),
    path('test_sub', views.test_sub),
    
    # http://127.0.0.1:8000/publishers/add_book
    path('add_book', views.add_book),
] 

urlpatterns += static(settings.STATIC_URL)

