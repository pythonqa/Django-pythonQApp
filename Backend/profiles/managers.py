from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

class UserManager(BaseUserManager):
    '''
    Our custom user manager need create two kind of account
    basic and superuser,remember we need create it with email field
    '''

    user = get_user_model()
    #Getting the user model,first it will try get it from settings.AUTH_USER_MODEL
    #if not will substitute it with django.contrib.auth.models User


    def _create_user(*args,**kwargs):
        pass

    def create_user(*args,**kwargs):
        pass

    def create_superuser(*args,**kwargs):
        pass

