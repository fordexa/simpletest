from django.http import HttpResponseRedirect, HttpResponse
from WindowsLiveLogin import WindowsLiveLogin
from django.core.urlresolvers import reverse

wll = WindowsLiveLogin.initFromXml('services/liveid/Application-Key.xml')

def webauth_handler(request):
    """
    Handler for WindowsLiveLogin login action
    """
    action = request.GET.get("action", None)
    if action == "logout":
        if "webauthtoken" in request.session:
            del request.session["webauthtoken"]
        return HttpResponseRedirect('/accounts/login/')
    elif action == "clearcookie":
        if "webauthtoken" in request.session:
            del request.session["webauthtoken"]
        return HttpResponse(wll.getClearCookieResponse())
    else:
        class Value(object):
            def __init__(self,value):
                self.value=value
        fs = dict()
        for key, val in request.POST.items():
            fs[key] = Value(val)
        
        user = wll.processLogin(fs)
        if user:
            request.session["webauthtoken"] = user.getToken()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/accounts/login/')
