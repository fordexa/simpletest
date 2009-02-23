"""
Main urls for outside auth
"""
from django.conf.urls.defaults import *

urlpatterns = patterns('simpletest.services',
    url(r'^google/$', 'google.views.login', name='google-auth'),
)
