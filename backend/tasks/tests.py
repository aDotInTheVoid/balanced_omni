from unittest import skip
from datetime import date

from django.test import TestCase
from django.db.models.deletion import ProtectedError

from .models import Kind, Task, Subtask
from backend.profiles.models import Profile
from backend.jwt_auth.models import User


class Deletions(TestCase):
    def setUp(self):
        User.objects.create_user("Foo", "")
        user = User.objects.get(username="Foo")
        prof = Profile.objects.get(user=user)
        kind = Kind.objects.create(name="Bar", author=prof, importance=5)
        task = Task.objects.create(name="Baz", assignee=prof, due_date=date.today(),
                                   is_done=False, author=prof, kind=kind)

    def test_delete_kind_raises_protected_error(self):
        self.assertRaises(ProtectedError, self.deleate_kind_bar)
        Task.objects.get().delete()
        self.deleate_kind_bar()

    def deleate_kind_bar(self):
        Kind.objects.get(name="Bar").delete()
