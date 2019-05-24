from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class UserProfileManager(BaseUserManager):
    """Help Django work with our custom model."""

    def create_user(self, email, name, password=None):
        """Create a new user profiles object."""

        if not email:
            raise ValueError('Users must have an email address.')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Creates and saves a new superuser with given details."""

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        
        user.save(using=self._db)

        return user


class UserProfiles(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""

        return self.name

    def get_short_name(self):
        """Retrieve shot name of user"""

        return self.name

    def __str__(self):
        """Return string representation of our user"""

        return self.email
    

class ProfileFeedItem(models.Model):
    """Profile status update."""

    user_profile = models.ForeignKey('UserProfiles', on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as a string"""

        return self.status_text