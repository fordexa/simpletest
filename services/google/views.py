from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.contrib.auth import login as django_login
from django.contrib.auth import authenticate
from utils.views import render_to
from simpletest.services.google.forms import LoginForm



@render_to('services/google.html')
def login(request):
    if request.POST:
        form = LoginForm(request.POST)
        if not form.is_valid():
            return {'form':form}
        try:
            email = form.cleaned_data['email']
            user = authenticate(email=email, password=form.cleaned_data['password'])
            if not user:
                return {'error': 'Your username and password were incorrect', 'form':form}
            django_login(request, user)
            return HttpResponseRedirect(request.GET.get('next', '/'))
        except Exception, ex:
            return {'error': str(ex), 'form':form}
    else:
        return {'form':LoginForm()}