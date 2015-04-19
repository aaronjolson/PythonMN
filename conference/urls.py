from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

urlpatterns = patterns('conference.views',
                       url(r'^$', 'home', name='home'),
                       url(r'signup/$', 'signup', name='signup'),
                       url(r'sponsors/$', 'sponsors', name='sponsors'),
                       url(r'about/$', 'about', name='about')
                       )