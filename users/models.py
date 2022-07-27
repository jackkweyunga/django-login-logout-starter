from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.management.utils import get_random_secret_key

from django.urls import reverse
from django.core.management.utils import get_random_secret_key


class User(AbstractUser):
    
    """
        A custom user model
    """
    username = models.CharField(unique=True, max_length=255, default="")
    phone_number = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(unique=True, db_index=True)
    secret_key = models.CharField(max_length=255, default=get_random_secret_key)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    class Meta:
        swappable = 'AUTH_USER_MODEL'
        
    
    def default_username(self):
        # creates a default username case not provided
        uname = self.email.split('@')[0]
        self.username = f"{uname}"
        
        
    def save(self, *args, **kwargs):
        
        if self.username == "":
            self.default_username
            
        super(User, self).save(*args, **kwargs)


    @property
    def name(self):
        """
            Returns a full name
        """
        if not self.last_name:
            return self.first_name.capitalize()

        return f'{self.first_name.capitalize()} {self.last_name.capitalize()}'
    
    
    def get_success_url(self):
        return reverse('users:user-update', kwargs={'pk': self.pk})


