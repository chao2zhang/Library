from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login, logout
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^login/$', login),
    url(r'^logout/$', logout),
    url(r'^register/$', 'registrations.views.register'),
    url(r'^reactivate/$', 'registrations.views.reactivate'), 
    url(r'^confirm/(\w{30})/$', 'registrations.views.confirm'),
    
    # Examples:
    # url(r'^$', 'library.views.home', name='home'),
    # url(r'^library/', include('library.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
