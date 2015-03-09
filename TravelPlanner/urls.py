import os

from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from TravelPlanner import settings


urlpatterns = patterns('',
    url(r'^flight/', include('FlightPlanner.urls', namespace='FlightPlanner')),
    url(r'^place/', include('PlacesPlanner.urls', namespace='PlacesPlanner')),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_URL)

