from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings


class UserProfileManager(BaseUserManager):
    """
    Manager for user profiles
    """

    def create_user(self, email, name, password=None, **extra_fields):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)  # second half lowercase
        user = self.model(email=email, name=name, **extra_fields)

        user.set_password(password)  # hash password
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    Database model for users
    """

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_activate = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    # Override default AbstractBaseUser fields
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of user"""
        return self.email


class ProfileFeedItem(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.TimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as a string"""
        return self.status_text
