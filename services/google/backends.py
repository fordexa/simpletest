"""
Google auth backend
"""
from django.contrib.auth.models import User
import gdata.service

class AuthService(gdata.service.GDataService):
    """
    Init Google service
    """
    def __init__(self, email=None, password=None, source='Test assignment', 
                 server='www.google.com', 
                 service=None,
                 additional_headers=None):
        gdata.service.GDataService.__init__(self, email=email, password=password,
                                            service=service, source=source, 
                                            server=server, 
                                            additional_headers=additional_headers) 

class Google:
    
    def _get_or_create_user(self, email):
        username = email
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return User.objects.create_user(username, email)
    
    def authenticate(self, email=None, password=None, service='cp'):
        try:
            gd_client = AuthService(email=email, password=password, service=service)
            gd_client.ProgrammaticLogin()
            return self._get_or_create_user(email)
        except Exception, ex:
            return None
    
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
