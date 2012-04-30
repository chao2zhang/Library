from django.conf.urls.defaults import patterns, url
from views import index, new, edit, delete, show, change_password, topup
urlpatterns = patterns('',
    url(r'^$', index),
    url(r'^new/$', new),
    url(r'^(\d+)/edit/$', edit),
    url(r'^(\d+)/delete/$', delete),
    url(r'^(\d+)/show/$', show),
    url(r'^(\d+)/change/$', change_password),
    url(r'^(\d+)/topup/$', topup),
)