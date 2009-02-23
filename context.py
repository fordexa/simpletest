"""
Template context for simpletest
"""
from simpletest.services.liveid import settings as wllsettings
from WindowsLiveLogin import WindowsLiveLogin


def wll_login_settings(request):
    """
    Return a windows liveid settings params for cunstruct login url
    """
    wll = WindowsLiveLogin.initFromXml('services/liveid/Application-Key.xml')
    return { 'wll_login_settings': wllsettings,
             'wllappid': wll.getAppId() }