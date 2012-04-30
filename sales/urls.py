from django.conf.urls.defaults import patterns, url
from views import index, new, delete, show
urlpatterns = patterns('',
    url(r'^$', index),
    url(r'^new/$', new),
    url(r'^(\d+)/delete/$', delete),
    url(r'^(\d+)/show/$', show),
)
