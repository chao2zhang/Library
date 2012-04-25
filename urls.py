from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login, logout
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^login/$', login),
    url(r'^logout/$', logout),
    url(r'^register/$', 'registrations.views.register'),
    url(r'^reactivate/$', 'registrations.views.reactivate'), 
    url(r'^confirm/(\w{30})/$', 'registrations.views.confirm'),
    url(r'^books/', include('books.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
