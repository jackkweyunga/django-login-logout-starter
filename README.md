# DJANGO LOGIN LOGOUT

A starter template for a django project requiring user account functionalities such as:

- [ ] user registration
- [ ] user registration API
- [ ] user registration with Social Accounts PLUS Api
- [ ] user session
- [ ] user session API

## Development

### Installations

Create a virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

python development requirements

```shell
python3 -m pip install -r requirements-dev.txt
```

css and js requirements / node modules.

```shell
npm i
```

### Environment Variables

Create a `.env` file to store your environment

- Require variables

~~~~~~~~~~

DEBUG=TRUE
SITE_ID=2
SITE_NAME="My Site"

DJANGO_ADMIN_USERNAME=""
DJANGO_ADMIN_EMAIL="" 
DJANGO_ADMIN_PASSWORD="" 

EMAIL_HOST_USER=""
EMAIL_HOST_PASSWORD=""


GOOGLE_CLIENT_ID=""
GOOGLE_CLIENT_SECRET=""
GOOGLE_CLIENT_KEY=""
GOOGLE_PROJECT_ID=""

ACCOUNT_DEFAULT_HTTP_PROTOCOL=""

~~~~~~~~~~

Fill in the values to according to your case. Google variables can be obtained from the `Google Developers Console`. Set Authorized redirect URIs as follows.
```
http://127.0.0.1:8000/accounts/google/login/callback/
```

In case your application uses `HTTPS` , set:
```
ACCOUNT_DEFAULT_HTTP_PROTOCOL="HTTPS"
```
Make sure the SITE ID corresponds to a site available in the database.


## Run the applications

Run Migrations

```shell
python3 -m python manage.py migrate
```

Create the django superuser

```shell
python3 -m python csu.py
```

Run the application

```shell
python3 -m python manage.py runserver
```
