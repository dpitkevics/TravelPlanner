from django.conf.urls import patterns, url

from FlightPlanner import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)