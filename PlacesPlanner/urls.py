from django.conf.urls import patterns, url

from PlacesPlanner import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^category-list$', views.category_list, name='category_list')
)