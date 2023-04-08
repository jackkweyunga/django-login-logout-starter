from django.dispatch import receiver
from users.models import User
from allauth.socialaccount.signals import social_account_added
@receiver(social_account_added)
def user_profile_update(request,sociallogin, **kwargs):
    """
    - edit user profile picture url and first & last name from current provider
    -- only tested in google authentication
    """
    try:
        data=sociallogin.account.extra_data
        update_fields={}
        if data:
            if not sociallogin.user.first_name:
                update_fields["first_name"]=data.get("given_name","")
            if not sociallogin.user.last_name:
                update_fields["last_name"]=data.get("family_name","")
            update_fields["profile_url"]=sociallogin.get_avatar_url()
            User.objects.filter(id=sociallogin.user.id).update(**update_fields)
    except Exception as e:
        print("data format from social provider is incompatible")
        pass