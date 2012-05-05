from django.conf.urls.defaults import patterns, url
from views import index, delete, show, new
urlpatterns = patterns('',
    url(r'^$', index),
    url(r'^(\d+)/delete/$', delete),
    url(r'^(\d+)/show/$', show),
    url(r'^(\d+)/new/$', new),
)