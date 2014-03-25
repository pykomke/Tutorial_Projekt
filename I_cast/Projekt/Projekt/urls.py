# Projekt/Projekt/urls.py/ -- verzia 0.1 Cast_1-kapitola
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
