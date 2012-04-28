from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login, logout
from django.contrib import admin
import settings
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'manage.views.home'),
    url(r'^login/$', login),
    url(r'^logout/$', logout),
    url(r'^register/$', 'registrations.views.register'),
    url(r'^reactivate/$', 'registrations.views.reactivate'), 
    url(r'^confirm/(\w{30})/$', 'registrations.views.confirm'),
    url(r'^books/', include('books.urls')),
    url(r'^members/', include('members.urls')),
    url(r'^purchases/', include('purchases.urls')),
    url(r'^groups/', include('groups.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
)
