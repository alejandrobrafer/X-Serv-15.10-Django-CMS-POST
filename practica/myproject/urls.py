"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from cms import views
from django.contrib.auth.views import logout, login
from django.views.generic import RedirectView

urlpatterns = [
	url(r'^logout', logout),
	url(r'^^login', login),
	url(r'^accounts/profile/', RedirectView.as_view(url='/', permanent=True)),
    url(r'^admin/', include(admin.site.urls)),
     url(r'^edit/(.+)$', views.edit),
    url(r'^annotated/(.+)$', views.annotated),
    url(r'(.+)', views.content),
    url(r'^$', views.principal),
]