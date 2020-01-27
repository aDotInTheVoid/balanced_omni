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
        self.user = User.objects.create_user("Foo", "f")
        self.prof = Profile.objects.get(user=self.user)
        Task.objects.create(name="notdone", author=self.prof,
                            due_date=date.today(), is_done=False)
        Task.objects.create(name="done", author=self.prof,
                            due_date=date.today(), is_done=True)
        self.client.force_authenticate(self.user)

    def test_use_filter(self):
        done_tasks = self.client.get('/api/tasks/?done=true')
        not_done_tasks = self.client.get('/api/tasks/?done=false')
        self.assertEqual(done_tasks.json()[0]['name'], 'done')
        self.assertEqual(not_done_tasks.json()[0]['name'], 'notdone')


class RestCreate(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user("Foo", "f")
        self.prof = Profile.objects.get(user=self.user)
        self.client.force_authenticate(self.user)

    def test_errors_on_empty(self):
        r = self.client.post('/api/tasks/')
        self.assertEqual(r.status_code, 400)
        j = r.json()
        errors = j.pop('errors')
        self.assertEqual(j, {})
        self.assertEqual(errors['name'], ['This field is required.'])
        self.assertEqual(errors['due_date'], ['This field is required.'])
        self.assertEqual(errors['is_done'], ['This field is required.'])

    def test_can_create(self):

        task_json = {'name': 'bax',
                     'due_date': '2023-02-01', 'is_done': True}

        r = self.client.post('/api/tasks/', task_json)
        self.assertEqual(r.status_code, 201)

        for i in task_json:
            self.assertEqual(r.json()[i], task_json[i])

        task = Task.objects.get(pk=r.json()['id'])
        self.assertEqual(task.name, 'bax')
        self.assertEqual(task.is_done, True)
        self.assertEqual(task.author, self.prof)
        self.assertEqual(task.due_date, date(2023, 2, 1))


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


class AnonUser(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user("Foo", "f")
        self.prof = Profile.objects.get(user=self.user)
        Task.objects.create(name="notdone", author=self.prof,
                            due_date=date.today(), is_done=False)
        self.client.credentials()

    def test_cant_read_tasks(self):
        r = self.client.get('/api/tasks/')
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['errors']['detail'],
                         'Authentication credentials were not provided.')
