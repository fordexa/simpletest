from django.conf.urls.defaults import *

urlpatterns = patterns('simpletest.profiles.views',
    url(r'^$', 'my_profile', name='my-profile'),
    url(r'^edit/$', 'edit_profile', name='edit-profile'),
)
