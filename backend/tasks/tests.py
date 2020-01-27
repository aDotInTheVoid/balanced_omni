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

class UpdateRest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user("Foo", "f")
        self.prof = Profile.objects.get(user=self.user)
        Task.objects.create(name="t1", author=self.prof,
                            due_date=date.today(), is_done=False)
        self.client.force_authenticate(self.user)

    def test_update_task(self):
        task_id = self.client.get('/api/tasks/').json()[0]['id']
        self.assertEqual(Task.objects.get(pk=task_id).is_done, False)
        task = self.client.patch(f"/api/tasks/{task_id}/", {"is_done": True})
        self.assertEqual(task.status_code, 200)
        self.assertEqual(Task.objects.get(pk=task_id).is_done, True)


class RestFilter(APITestCase):
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
