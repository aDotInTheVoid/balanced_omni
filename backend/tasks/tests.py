from datetime import date

# from django.db.models.deletion import ProtectedError

from rest_framework.test import APITestCase

from backend.profiles.models import Profile
from backend.jwt_auth.models import User
from .models import Task


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

class RestRead(APITestCase):
    def setUp(self):
        User.objects.create_user("Foo", "f")
        self.user1 = User.objects.get(username="Foo")
        self.prof1 = Profile.objects.get(user=self.user1)
        Task.objects.create(name="t1", author=self.prof1,
                            due_date=date.today(), is_done=False)

        User.objects.create_user("Bar", "b")
        self.user2 = User.objects.get(username="Bar")
        self.prof2 = Profile.objects.get(user=self.user2)
        Task.objects.create(name="t2", author=self.prof2,
                            due_date=date.today(), is_done=True)

    def test_get_task_list(self):
        self.client.force_authenticate(self.user1)
        r1 = self.client.get('/api/tasks/')
        self.assertEqual(r1.status_code, 200)
        j1 = r1.json()
        self.assertEqual(len(j1), 1)
        self.assertEqual(j1[0]['name'], 't1')
        self.assertEqual(j1[0]['is_done'], False)

        self.client.force_authenticate(self.user2)
        r2 = self.client.get('/api/tasks/')
        self.assertEqual(r1.status_code, 200)
        j2 = r2.json()
        self.assertEqual(len(j2), 1)
        self.assertEqual(j2[0]['name'], 't2')
        self.assertEqual(j2[0]['is_done'], True)
