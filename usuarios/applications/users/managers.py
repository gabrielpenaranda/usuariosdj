from django.db import models
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    
    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username = username,
            email = email,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_user(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False, **extra_fields)
        
    def create_superuser(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, True, True, **extra_fields)
        
    """ def create_user(self, username, email, password, is_staff=False):
        user = self.model(
            username = username,
            email = self.normalize_email(email), 
            is_staff = is_staff
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            username = username,
            email=email,
            password = password,
            is_staff = True
        )

        user.is_superuser = True
        user.save(using=self._db)

        return user """