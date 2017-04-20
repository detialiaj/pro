"""SYS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from main import views as main_views
from inout import views as inout_views

urlpatterns = [
    url(r'^$', main_views.dashboard, name='dashboard'), # Temporary - redirect to the admin site until main-home-page is created
    url(r'^manage/', include(admin.site.urls)),
    url(r'^main/', include('main.urls'), name='main_home'),
    url(r'^inout/', include('inout.urls')),
    # url(r'^inout/', main_views.no_page_yet, name='no_page'), #can't raise a 404 page with DEBUG=True
]
