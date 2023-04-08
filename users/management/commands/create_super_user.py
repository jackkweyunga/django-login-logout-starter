import os
import django
from decouple import config
from django.contrib.auth import get_user_model

os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings"
django.setup()

from allauth.account.models import EmailAddress

User = get_user_model()
from django.core.management import BaseCommand


class Command(BaseCommand):
    # Show this when the user types help
    help = "use python manage.py create_super_user with flags 'flupe' -f,-l,-u,-p and -e for first_name,last_name,username,password and email respectively.if not provided they will be fetched from .env "

    def add_arguments(self, parser) -> None:
        parser.add_argument(
            "-u",
            "--username",
            type=str,
            nargs="?",
            default=config("DJANGO_ADMIN_USERNAME"),
            help="superuser username",
        )

        parser.add_argument(
            "-p",
            "--password",
            type=str,
            nargs="?",
            default=config("DJANGO_ADMIN_PASSWORD"),
            help="superuser password",
        )

        parser.add_argument(
            "-e",
            "--email",
            type=str,
            nargs="?",
            default=config("DJANGO_ADMIN_EMAIL"),
            help="superuser email",
        )

        parser.add_argument(
            "-f",
            "--first_name",
            type=str,
            nargs="?",
            default=config("DJANGO_ADMIN_FIRSTNAME", default=""),
            help="superuser first name",
        )

        parser.add_argument(
            "-l",
            "--last_name",
            type=str,
            nargs="?",
            default=config("DJANGO_ADMIN_LASTNAME", default=""),
            help="superuser last name",
        )

        return super().add_arguments(parser)

    def handle(self, *args, **kwargs):

        password = kwargs["password"]
        username = kwargs["username"]
        email = kwargs["email"]
        first_name = kwargs["first_name"]
        last_name = kwargs["last_name"]
        self.stdout.write(
                    self.style.HTTP_NOT_MODIFIED(f"first_name: {first_name},\nlast_name: {last_name},\nusername: {username},\npassword: {password},\nemail: {email},\nHINT:MNEMONIC-flupe")
                )
        update_fields = {}
        try:
            user = User.objects.get(email=email)
            """
                -- either created in above command or alredy exists 
                -- make user superuser and staff as he might be existing as normal user
            """
            self.stdout.write(self.style.WARNING(f"User:{email} already exists...!"))
            # incase user exists he is updated as staff and superuser
            update_fields["is_superuser"] = True
            update_fields["is_staff"] = True
            if not user.first_name:
                self.stdout.write(
                    self.style.WARNING(f"first name updated to {first_name}")
                )

                update_fields["first_name"] = first_name
            if not user.last_name:
                self.stdout.write(
                    self.style.WARNING(f"last name updated to {last_name}")
                )

                update_fields["last_name"] = last_name
            User.objects.filter(id=user.id).update(**update_fields)
            self.stdout.write(self.style.SUCCESS(f"User: {email} updated successfully"))

        except User.DoesNotExist:
            # if user does not exist assign appropriate values
            self.stdout.write(self.style.WARNING(f"User: {email} does not exist..!"))
            update_fields["username"] = username
            update_fields["email"] = email
            update_fields["first_name"] = first_name
            update_fields["last_name"] = last_name
            update_fields["password"] = password
            user = User.objects.create_superuser(**update_fields)
            self.stdout.write(
                self.style.SUCCESS(
                    f"Super user created with username {user.username} email {user.email} password ****** provided in the .env file or -p flag"
                )
            )
        if not EmailAddress.objects.filter(user=user.pk).exists():
            email = EmailAddress.objects.create(
                user=user, email=email, verified=True, primary=True
            )
            self.stdout.write(
                self.style.SUCCESS(f"activating superuser email email:{email}")
            )
