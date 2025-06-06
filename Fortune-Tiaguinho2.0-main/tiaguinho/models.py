from django.db import models
import uuid
from django.core.validators import MinLengthValidator 
from django.contrib.auth.hashers import make_password

class Users(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False,unique=True)
    nickname = models.CharField(max_length=20, validators=[MinLengthValidator(3)] , blank=False, unique=True)
    password = models.CharField(max_length=30, validators=[MinLengthValidator(8)])
    
    def save(self,*args,**kwargs):
        if not self.password.startswith('zeyreD_'):
            self.password=make_password(self.password)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.nickname



