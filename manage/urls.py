from django.conf.urls.defaults import patterns, include, url
urlpatterns = patterns('',
    url(r'^manage/$', include(manage.urls)),
    url(r'^admin/$', include(admin.site.urls)),
)