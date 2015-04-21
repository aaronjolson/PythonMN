from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^', include('conference.urls', namespace='conference')),
                       )

if settings.DEBUG:
    urlpatterns += patterns(
        url(r'', include('django.contrib.staticfiles.urls')),
    )
