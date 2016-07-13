"""Django_project URL Configuration
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
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from rango import views
from registration.backends.simple.views import RegistrationView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$', views.about, name='about'),
    #url(r'^$', views.custom, name='custom'),
    url(r'^rango/', include('rango.urls')),
    # above maps any URLs starting
    # with rango/ to be handled by
    # the rango application
    url(r'^admin/', admin.site.urls),
    # Create a new class that redirects the user to the index page, if
    # successful at logging
    url(r'^accounts/', include('registration.backends.simple.urls')),


]


class MyRegistrationView(RegistrationView):

    def get_success_url(self, request, user):
        return '/rango/'
