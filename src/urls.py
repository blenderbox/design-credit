import os, sys

from django.conf import settings
from django.contrib import admin
from django.conf.urls.defaults import *


admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^news/', include('news.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    # Temp Hello World, you can delete this
    (r'^$', 'django.views.generic.simple.direct_to_template', {'template':'hello-world.html'}),
)

if getattr(settings, 'LOCAL_SERVE', False):
    urlpatterns = patterns('django.views.static',
	url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL.lstrip('/'), 'serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    ) + staticfiles_urlpatterns() + urlpatterns
