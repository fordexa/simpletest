from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from simpletest.profiles.forms import EditProfileForm
from django.contrib.auth.decorators import login_required
from registration.models import RegistrationProfile

@login_required
def my_profile(request):
    profile = get_object_or_404(RegistrationProfile, user=request.user)
    return render_to_response('profiles/my.html',
                              {'user': profile.user},
                              RequestContext(request))

@login_required
def edit_profile(request):
    if request.POST:
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            new_profile = form.save()
            return HttpResponseRedirect(reverse('my-profile'))
        else:
            return render_to_response('profiles/edit.html',
                                      {'form': form},
                                      RequestContext(request))
    else:
        form = EditProfileForm(instance=request.user)
        return render_to_response('profiles/edit.html',
                                  {'form': form},
                                  RequestContext(request))
        

