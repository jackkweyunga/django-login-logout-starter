import os
import logging
import django
from decouple import config
from django.contrib.auth import get_user_model

os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings"
django.setup()

from allauth.account.models import EmailAddress

User = get_user_model()


def create_super_user(
    password=config("DJANGO_ADMIN_PASSWORD"),
    username=config("DJANGO_ADMIN_USERNAME"),
    email=config("DJANGO_ADMIN_EMAIL"),
    first_name=config("DJANGO_ADMIN_FIRSTNAME", default=""),
    last_name=config("DJANGO_ADMIN_LASTNAME", default=""),
):
    update_fields = {}
    try:
        user = User.objects.get(email=email)
        """
            -- either created in above command or alredy exists 
            -- make user superuser and staff as he might be existing as normal user
        """
        print("This user already exists...!")
        # incase user exists he is updated as staff and superuser
        update_fields["is_superuser"] = True
        update_fields["is_staff"] = True
        if not user.first_name:
            print(f"first name updated to {first_name}")
            update_fields["first_name"] = first_name
        if not user.last_name:
            print(f"last name updated to {last_name}")
            update_fields["last_name"] = last_name
        User.objects.filter(id=user.id).update(**update_fields)
        print("User updated successfully")
    except User.DoesNotExist:
        # if user does not exist assign appropriate values
        print("user does not exist")
        update_fields["username"] = username
        update_fields["email"] = email
        update_fields["first_name"] = first_name
        update_fields["last_name"] = last_name
        update_fields["password"] = password
        user = User.objects.create_superuser(**update_fields)
        print(
            f"Super user created with username {user.username} email {user.email} password ******"
        )
    if not EmailAddress.objects.filter(user=user.pk).exists():
        email = EmailAddress.objects.create(user=user, email=email, verified=True, primary=True
        )
        print(f"activating superuser email email:{email}")


create_super_user()
