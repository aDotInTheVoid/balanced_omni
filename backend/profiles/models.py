from django.db import models

from backend.core.models import TimestampedModel


class Profile(TimestampedModel):
    # There is an inherent relationship between the Profile and
    # User models. By creating a one-to-one relationship between the two, we
    # are formalizing this relationship. Every user will have one -- and only
    # one -- related Profile model.
    user = models.OneToOneField(
        'jwt_auth.User', on_delete=models.CASCADE
    )

    #TODO: CHANGEME

    # Each user profile will have a field where they can tell other users
    # something about themselves. This field will be empty when the user
    # creates their account, so we specify blank=True.
    bio = models.TextField(blank=True)

    # In addition to the `bio` field, each user may have a profile image or
    # avatar. This field is not required and it may be blank.
    image = models.URLField(blank=True)

    @staticmethod
    def username(self):
        return self.user.username

    def __str__(self):
        return self.user.username
