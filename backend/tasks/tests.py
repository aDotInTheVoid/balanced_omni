from datetime import date

# from django.db.models.deletion import ProtectedError

from rest_framework.test import APITestCase
from rest_framework.status import *

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


###
# CRUD Main Tests
class RestCreate(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user("Foo", "f")
        self.prof = Profile.objects.get(user=self.user)
        self.client.force_authenticate(self.user)

    def test_errors_on_empty(self):
        r = self.client.post('/api/tasks/')
        self.assertEqual(r.status_code, HTTP_400_BAD_REQUEST)
        j = r.json()
        errors = j.pop('errors')
        self.assertEqual(j, {})
        self.assertEqual(errors['name'], ['This field is required.'])
        self.assertEqual(errors['due_date'], ['This field is required.'])
        self.assertEqual(errors['is_done'], ['This field is required.'])

    def test_can_create(self):

        task_json = {'name': 'bax',
                     'due_date': '2023-02-01', 'is_done': True, 'priority': 4, 'importance': -2}

        r = self.client.post('/api/tasks/', task_json)
        self.assertEqual(r.status_code, HTTP_201_CREATED)

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
                            due_date=date.today(), is_done=False,
                            priority=2, importance=3)

        User.objects.create_user("Bar", "b")
        self.user2 = User.objects.get(username="Bar")
        self.prof2 = Profile.objects.get(user=self.user2)
        Task.objects.create(name="t2", author=self.prof2,
                            due_date=date.today(), is_done=True, priority=2, importance=3)

    def test_get_task_list(self):
        self.client.force_authenticate(self.user1)
        r1 = self.client.get('/api/tasks/')
        self.assertEqual(r1.status_code, HTTP_200_OK)
        j1 = r1.json()
        self.assertEqual(len(j1), 1)
        self.assertEqual(j1[0]['name'], 't1')
        self.assertEqual(j1[0]['is_done'], False)
        self.assertEqual(j1[0]['priority'], 2)
        self.assertEqual(j1[0]['importance'], 3)

        self.client.force_authenticate(self.user2)
        r2 = self.client.get('/api/tasks/')
        self.assertEqual(r1.status_code, HTTP_200_OK)
        j2 = r2.json()
        self.assertEqual(len(j2), 1)
        self.assertEqual(j2[0]['name'], 't2')
        self.assertEqual(j2[0]['is_done'], True)
        self.assertEqual(j2[0]['priority'], 2)
        self.assertEqual(j2[0]['importance'], 3)


class RestUpdate(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user("Foo", "f")
        self.prof = Profile.objects.get(user=self.user)
        Task.objects.create(name="t1", author=self.prof,
                            due_date=date.today(), is_done=False, priority=2, importance=3)
        self.client.force_authenticate(self.user)

    def test_update_task(self):
        task_id = self.client.get('/api/tasks/').json()[0]['id']
        self.assertEqual(Task.objects.get(pk=task_id).is_done, False)
        task = self.client.patch(f"/api/tasks/{task_id}/", {"is_done": True})
        self.assertEqual(task.status_code, HTTP_200_OK)
        self.assertEqual(Task.objects.get(pk=task_id).is_done, True)


class RestDeleat(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user("Foo", "f")
        self.prof = Profile.objects.get(user=self.user)
        Task.objects.create(name="t1", author=self.prof,
                            due_date=date.today(), is_done=False, priority=2, importance=3)
        self.client.force_authenticate(self.user)

    def test_delete(self):
        self.assertNotEqual(Task.objects.all().count(), 0)
        task_id = self.client.get('/api/tasks/').json()[0]['id']
        responce = self.client.delete(f'/api/tasks/{task_id}/')
        self.assertEqual(responce.status_code, HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.all().count(), 0)


class RestFilter(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user("Foo", "f")
        self.prof = Profile.objects.get(user=self.user)
        Task.objects.create(name="notdone", author=self.prof,
                            due_date=date.today(), is_done=False, priority=2, importance=3)
        Task.objects.create(name="done", author=self.prof,
                            due_date=date.today(), is_done=True, priority=2, importance=3)
        self.client.force_authenticate(self.user)

    def test_use_filter(self):
        done_tasks = self.client.get('/api/tasks/?done=true')
        not_done_tasks = self.client.get('/api/tasks/?done=false')
        self.assertEqual(done_tasks.json()[0]['name'], 'done')
        self.assertEqual(not_done_tasks.json()[0]['name'], 'notdone')

    def test_bad_filter(self):
        responce = self.client.get('/api/tasks/?done=bb')
        self.assertEqual(responce.status_code, HTTP_400_BAD_REQUEST)


class AnonUser(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user("Foo", "f")
        self.prof = Profile.objects.get(user=self.user)
        Task.objects.create(name="notdone", author=self.prof,
                            due_date=date.today(), is_done=False, priority=2, importance=3)
        self.client.logout()

    def test_cant_read_tasks(self):
        r = self.client.get('/api/tasks/')
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['errors']['detail'],
                         'Authentication credentials were not provided.')


class MultiUserStuff(APITestCase):
    def setUp(self):
        self.user_f = User.objects.create_user("Foo", "f")
        self.prof_f = Profile.objects.get(user=self.user_f)
        Task.objects.create(name="f", author=self.prof_f,
                            due_date=date.today(), is_done=False, priority=2, importance=3)

        self.user_b = User.objects.create_user("Bar", "b")
        self.prof_b = Profile.objects.get(user=self.user_b)
        Task.objects.create(name="b", author=self.prof_b,
                            due_date=date.today(), is_done=False, priority=2, importance=3)

        self.client.force_authenticate(self.user_f)
        self.id_f = self.client.get('/api/tasks/').json()[0]['id']

        self.client.force_authenticate(self.user_b)
        self.id_b = self.client.get('/api/tasks/').json()[0]['id']

    def test_tasks_id_neq(self):
        self.assertNotEqual(self.id_b, self.id_f)

    def test_each_can_get_self_by_list(self):
        self.client.force_authenticate(self.user_f)
        resp_f = self.client.get('/api/tasks/')
        self.assertEqual(resp_f.status_code, HTTP_200_OK)
        json_f = resp_f.json()
        self.assertEqual(len(json_f), 1)
        self.assertEqual(json_f[0]["name"], "f")

        self.client.force_authenticate(self.user_b)
        resp_b = self.client.get('/api/tasks/')
        self.assertEqual(resp_b.status_code, HTTP_200_OK)
        json_b = resp_b.json()
        self.assertEqual(len(json_b), 1)
        self.assertEqual(json_b[0]["name"], "b")

    def test_each_can_get_self_by_id(self):
        self.client.force_authenticate(self.user_f)
        resp_f = self.client.get(f'/api/tasks/{self.id_f}/')
        self.assertEqual(resp_f.status_code, HTTP_200_OK)
        self.assertEqual(resp_f.json()["name"], "f")

        self.client.force_authenticate(self.user_b)
        resp_b = self.client.get(f'/api/tasks/{self.id_b}/')
        self.assertEqual(resp_b.status_code, HTTP_200_OK)
        self.assertEqual(resp_b.json()["name"], "b")

    def test_each_cant_get_other(self):
        for (user, task_id, sc) in [
            (self.user_b, self.id_b, HTTP_200_OK),
            (self.user_f, self.id_f, HTTP_200_OK),
            (self.user_b, self.id_f, HTTP_404_NOT_FOUND),
            (self.user_f, self.id_b, HTTP_404_NOT_FOUND),
        ]:
            self.client.force_authenticate(user)
            self.assertEqual(self.client.get(
                f'/api/tasks/{task_id}/').status_code,
                sc
            )
