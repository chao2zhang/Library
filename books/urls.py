from django.conf.urls.defaults import patterns, url
from views import index, new, edit, delete, show
urlpatterns = patterns('',
    url(r'^$', index),
    url(r'^new/$', new),
    url(r'^(?P<id>\d+)/edit/$', edit),
    url(r'^(?P<id>\d+)/delete/$', delete),
    url(r'^(?P<id>\d+)/show/$', show),
)