"""
Main site URL patterns
"""
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf import settings 

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('registration.urls')),
    (r'^accounts/profile/', include('simpletest.profiles.urls')),
    (r'^services/', include('simpletest.services.urls')),
    url(r'^webauth/sample/webauth-handler.cgi',
        'simpletest.services.liveid.views.webauth_handler',
        name='liveid-handler'),
)

urlpatterns += patterns('',
    url(r'^$', 'simpletest.views.index', name='index'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
