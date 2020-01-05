from unittest import skip
from datetime import date

from django.test import TestCase, Client
from django.db.models.deletion import ProtectedError

from .models import Task
from backend.profiles.models import Profile
from backend.jwt_auth.models import User


# class Deletions(TestCase):
#     def setUp(self):
#         User.objects.create_user("Foo", "")
#         user = User.objects.get(username="Foo")
#         prof = Profile.objects.get(user=user)
#         kind = Kind.objects.create(name="Bar", author=prof, importance=5)
#         task = Task.objects.create(name="Baz", assignee=prof, due_date=date.today(),
#                                    is_done=False, author=prof, kind=kind)

#     def test_delete_kind_raises_protected_error(self):
#         self.assertRaises(ProtectedError, self.deleate_kind_bar)
#         Task.objects.get().delete()
#         self.deleate_kind_bar()

#     def deleate_kind_bar(self):
#         Kind.objects.get(name="Bar").delete()

class CrudRest(TestCase):
    @classmethod
    def setUp(self):
        User.objects.create_user("Foo", "f")
        self.user1 = User.objects.get(username="Foo")
        self.prof1 = Profile.objects.get(user=self.user1)
        self.token1 = self.user1.token
        Task.objects.create(name="t1", author=self.prof1, due_date=date.today(), is_done=False)

        User.objects.create_user("Bar", "b")
        self.user2 = User.objects.get(username="Bar")
        self.prof2 = Profile.objects.get(user=self.user2)
        self.token2 = self.user2.token
        Task.objects.create(name="t2", author=self.prof2, due_date=date.today(), is_done=True)

        self.client = Client()

    def test_get_task(self):
        tasks = self.client.get('/api/tasks/', HTTP_AUTHORIZATION="Token "+self.token1)
        print(tasks.content)

        tasks = self.client.get('/api/tasks/', HTTP_AUTHORIZATION="Token "+self.token2)
        print(tasks.content)
        #TODO: filter so only a users tasks gets displayed