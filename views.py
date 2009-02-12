from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):
    """
    Response to main project page
    """
    return render_to_response('base.html', {}, RequestContext(request))
