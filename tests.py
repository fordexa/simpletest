from nose.tools import *
from twill.commands import *
from twill import add_wsgi_intercept

IP = '127.0.0.1'
PORT = 8000
SITE = 'http://%s:%s' % (IP, PORT)

def setup():
    import os
    os.environ["DJANGO_SETTINGS_MODULE"] = "simpletest.settings"

    from django.core.servers.basehttp import AdminMediaHandler
    from django.core.handlers.wsgi import WSGIHandler

    app = AdminMediaHandler(WSGIHandler())
    add_wsgi_intercept("127.0.0.1", 9876, lambda: app)

@with_setup(setup)
def test_success_login():
    go(SITE + '/accounts/login/')
    code(200)
    show()
    formvalue(1, 'username',  'test')
    formvalue(1, 'password', '1')
    submit()
    code(200)
    find('<h4 align="center">My profile</h4>')
    return

@with_setup(setup)
def test_incorrect_password():
    go(SITE + '/accounts/login/')
    code(200)
    show()
    formvalue(1, 'username',  'test')
    formvalue(1, 'password', '123')
    submit()
    code(200)
    find('Please enter a correct username and password.')
    return

@with_setup(setup)
def test_incorrect_username():
    go(SITE + '/accounts/login/')
    code(200)
    show()
    formvalue(1, 'username',  'testincorrect')
    formvalue(1, 'password', '1')
    submit()
    code(200)
    find('Please enter a correct username and password.')
    return

@with_setup(setup)
def test_profile_record():
    go(SITE + '/accounts/login/')
    code(200)
    show()
    formvalue(1, 'username',  'root')
    formvalue(1, 'password', '1')
    submit()
    code(200)

@with_setup(setup)
def test_reset_password():
    go(SITE + '/accounts/password/reset/')
    code(200)
    show()
    formvalue(1, 'email',  'demo@system.mail')
    submit()
    code(200)
    find('Password reset successful')
    return

@with_setup(setup)
def test_change_password():
    go(SITE + '/accounts/login/')
    code(200)
    show()
    formvalue(1, 'username',  'test')
    formvalue(1, 'password', '1')
    submit()
    code(200)
    go(SITE + '/accounts/password/change/')
    code(200)
    show()
    formvalue(1, 'old_password',  '1')
    formvalue(1, 'new_password1',  '2')
    formvalue(1, 'new_password2',  '2')
    submit()
    code(200)
    find('Password change successful')
    go(SITE + '/accounts/login/')
    code(200)
    show()
    formvalue(1, 'username',  'test')
    formvalue(1, 'password', '2')
    submit()
    code(200)
    return

@with_setup(setup)
def test_register():
    go(SITE + '/accounts/register/')
    code(200)
    show()
    formvalue(1, 'username',  'demouser')
    formvalue(1, 'email',  'admin@system.mail')
    formvalue(1, 'password1',  '1')
    formvalue(1, 'password2',  '1')
    submit()
    code(200)
    find('Confirmation e-mail sent')
    return
