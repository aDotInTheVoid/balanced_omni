from django.apps import AppConfig


class AuthenticationAppConfig(AppConfig):
    name = 'backend.jwt_auth'
    label = 'jwt_auth'
    verbose_name = 'JSON Web Token Authentication'

    def ready(self):
        import backend.jwt_auth.signals


# This is how we register our custom app config with Django. Django is smart
# enough to look for the `default_app_config` property of each registered app
# and use the correct app config based on that value.
default_app_config = 'backend.jwt_auth.AuthenticationAppConfig'
