from django.dispatch import receiver
from users.models import User
from allauth.socialaccount.signals import social_account_added


@receiver(social_account_added)
def update_user_profile_on_social_account_added(request, sociallogin, **kwargs):
    """
    -> Objective:
        - To update the user profile when a social account is added.\n
    -> Flow:
        - Extracts extra data from the social login account
        - Checks if the user has provided a first name, last name, and profile picture URL
        - If not, updates the user's profile with the corresponding data from the social login account
    """
    data = sociallogin.account.extra_data
    update_fields = {}
    if data:
        # fetch username from google account when user provides no name
        if not sociallogin.user.first_name:
            update_fields["first_name"] = data.get("given_name", "")
        if not sociallogin.user.last_name:
            update_fields["last_name"] = data.get("family_name", "")
        update_fields["profile_pic_url"] = data.get("picture", "")
        User.objects.filter(id=sociallogin.user.id).update(**update_fields)
