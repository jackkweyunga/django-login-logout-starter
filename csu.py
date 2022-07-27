
# Python django script for creating superuser

from django.conf import settings
import django
import os
from decouple import config

os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings"

django.setup()

from users.models import User

try:
    from allauth.account.models import EmailAddress
except:
    print("All auth is not Implemented: ")


def createSuperUser( password=config("DJANGO_ADMIN_PASSWORD"), username=config("DJANGO_ADMIN_USERNAME"), email = config("DJANGO_ADMIN_EMAIL"), firstName = "", lastName = ""):

    try:
        user = User.objects.get(username="admin")
        return None
    except:
        pass

    user = User(
        username = username,
        email = email,
        first_name = firstName,
        last_name = lastName,
    )
    user.set_password(password)
    user.is_superuser = True
    user.is_staff = True
    user.save()

    try:    
        super_email = EmailAddress(user, user.email, True, True) 
        super_email.save()
    except:
        print("Super email not created: ")
    
    return user

createSuperUser()
