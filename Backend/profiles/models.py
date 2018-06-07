from PIL import Image
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from . import managers

class User(AbstractBaseUser):
    '''
    Custom User model extending the AbstractBaseUser,
    need have email required field,is_admin,is_staff,
    username optional and need use email for authentication
    User must provide UserManager custom manager extended from the 
    BaseUserManager
    '''
    pass


class Profile(models.Model):
    '''
    Profile model extended from the User class,need have
    info about user and need include avatar which must take image 
    and turn it into 280x280 thumbnail photo
    '''
    pass    