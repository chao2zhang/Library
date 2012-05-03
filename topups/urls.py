from django.conf.urls.defaults import patterns, url
from views import index, delete
urlpatterns = patterns('',
    url(r'^$', index),
    url(r'^(\d+)/delete/$', delete),
)