"""
Forms suite for managing accounts
"""
from django import forms
from django.contrib.auth.models import User


class EditProfileForm(forms.ModelForm):
    """
    Form for edit existing user profile
    """
    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
    class Meta:
        """
        Edit form meta options
        """
        model = User
        fields = ('first_name', 'last_name', 'username')
