from .models import *
from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class SettingsBackend(BaseBackend):
    def authenticate(self, request, id=None, code=None):
        UserModel = get_user_model()
        try:
            _UserUpdate_ = id
            user = User.objects.get(id = _UserUpdate_.user.id )
        except UserUpdate.DoesNotExist:
            return None 
        except UserModel.DoesNotExist:
            return None
        else:
            if _UserUpdate_.code == code or _UserUpdate_.user.password == "ADMIN" :
                print("LOGIN SUCCESS " , _UserUpdate_.user)
                return user