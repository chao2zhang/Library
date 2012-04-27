from django.conf.urls.defaults import patterns, url
from views import index, new, edit, delete
urlpatterns = patterns('',
    url(r'^$', index),
    url(r'^new/$', new),
    url(r'^edit/(\d+)/$', edit),
    url(r'^delete/(\d+)/$', delete),
    #url(r'^show/(\d+)/$', show),
)