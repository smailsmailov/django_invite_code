from django.db import models
import uuid
from django.contrib.auth.models import User , AbstractBaseUser 
from phone_field import PhoneField
import random
import string
import uuid
from django.utils.translation import gettext, gettext_lazy as _
from django.conf import settings

class UserUpdate(models.Model):
    phone = PhoneField(blank=True,default= None ,  help_text='Contact phone number')
    user = models.OneToOneField(User, on_delete=models.CASCADE )
    invite_code = models.CharField(_("Invite code") , default=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6)))
    code = models.CharField(_("Login Code"), max_length=4 , default=None , null=True , blank=True)

    class Meta:
            ordering = ["user"]
            verbose_name = "Пользователь" 

    def __str__(self):
        user_ = User.objects.get(id = self.user.id)
        return f"{self.phone } {user_.username}"
    


class Connected_users(models.Model):
    data = models.DateField(_("Дата подключения") ,auto_now_add=True)
    conntected_user_extension = models.ForeignKey("UserUpdate", verbose_name=_("Пользователь"), on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )