from django.conf.urls.defaults import patterns, url
from views import index
urlpatterns = patterns('',
    url(r'^$', index),
)
