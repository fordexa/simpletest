"""
URL patterns for manage user account
"""
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('simpletest.profiles.views',
    url(r'^$', 'my_profile', name='my-profile'),
    url(r'^edit/$', 'edit_profile', name='edit-profile'),
)
