"""mysite URL Configuration

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
from django.contrib import admin
from seasonal.views import home_view, browse_produce_view, browse_locations_view, search_view, faq_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_view, name="home"),
    url(r'^home/$', home_view, name="home"),
    url(r'^browse_produce/$', browse_produce_view, name="browse_produce"),
    url(r'^browse_locations/$', browse_locations_view, name="browse_locations"),
    url(r'^search/$', search_view, name="search"),
    url(r'^faq/$', faq_view, name="faq"),
]
