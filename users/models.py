from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.management.utils import get_random_secret_key
from django.urls import reverse
from django.core.management.utils import get_random_secret_key
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.db.models.functions import Lower


class User(AbstractUser):

    """
    A custom user model
    """

    username = models.CharField(
        max_length=50, validators=[ASCIIUsernameValidator()], unique=True, default=""
    )

    phone_number = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(unique=True, db_index=True)
    profile_pic_url = models.CharField(max_length=255, default="")

    secret_key = models.CharField(max_length=255, default=get_random_secret_key)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        swappable = "AUTH_USER_MODEL"
        constraints = [
            models.UniqueConstraint(
                Lower("email"),
                name="unique_lowercased_email",
            ),
            models.UniqueConstraint(
                Lower("username"),
                name="unique_lowercased_username",
            ),
            # ensure username is unique in a case insensitive way
            # for example User,user,USer and USeR are considered the same username
        ]

    @property
    def default_profile_pic_url(self) -> str:
        name = (
            f"{self.first_name}+{self.last_name}"
            if self.first_name and self.last_name
            else self.username
        )

        url = f"https://eu.ui-avatars.com/api/?name={name}&size=250&background=0D8ABC&color=fff&"
        return url
    @property
    def default_username(self) -> str:
        # creates a default username case not provided
        # ensures character do not exceed 50
        return self.email.split("@")[0][:50]

    def save(self, *args, **kwargs):
        # check username and profile picture and set appropriate values if undefined
        if not self.username:
            self.username = self.default_username
        if not self.profile_pic_url:
            self.profile_pic_url = self.default_profile_pic_url
        super().save(*args, **kwargs)

    @property
    def name(self) -> str:
        """
        Returns a full name
        """
        if self.first_name and self.last_name:
            full_name = f"{self.first_name} {self.last_name}"
        else:
            full_name = self.first_name or self.last_name
        return full_name

    # model urls
    def get_absolute_url(self):
        return self.get_detail_url()

    def get_detail_url(self) -> str:
        """
        Returns a url for viewing user details
        Returns:
            str: url
        """
        return reverse("users:user-detail", kwargs={"pk": self.pk})

    def get_update_url(self) -> str:
        """returns a url for updating a user

        Returns:
            str: url
        """

        return reverse("users:user-update", kwargs={"pk": self.pk})

    def get_list_url(self) -> str:
        """
        Returns a url for viewing a list of users

        Returns:
            str: url
        """
        return reverse("users:user-list")

    def get_success_url(self) -> str:
        return self.get_detail_url()
