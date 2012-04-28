from django.conf.urls.defaults import patterns, url
from views import index, new
urlpatterns = patterns('',
    url(r'^$', index),
    url(r'^new/$', new),
)
