from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('registration.urls')),
    (r'^accounts/profile/', include('simpletest.profiles.urls')),
)

urlpatterns += patterns('',
    url(r'^$', 'simpletest.views.index', name='index'),
)
