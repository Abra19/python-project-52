from django.test import TestCase, Client
from django.urls import reverse_lazy

from task_manager.users.models import User


class UsersTest(TestCase):
    fixtures = ['users.json']
    test_user = {
          'username': 'Test',
          'first_name': 'Test',
          'last_name': 'Test',
          'password1': '123',
          'password2': '123',
        }

    def setUp(self) -> None:
        self.client = Client()
        self.user1 = User.objects.get(pk=1)
        self.user2 = User.objects.get(pk=2)
        self.user3 = User.objects.get(pk=3)

    def test_users(self) -> None:
        response = self.client.get(reverse_lazy('users'))
        users_list = list(response.context['users'])
        user1, user2, user3 = users_list

        self.assertTrue(len(users_list) == 3)
        self.assertEqual(user1.username, 'Galois')
        self.assertEqual(user2.username, 'Abel')
        self.assertEqual(user3.username, 'Fermat')

    def test_users_list(self):
        response = self.client.get(reverse_lazy('users'))

        self.assertTemplateUsed(response, template_name='users/list.html')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, reverse_lazy('create'))
        self.assertContains(response, self.user1.first_name)
        self.assertContains(response, self.user2.last_name)
        self.assertContains(response, self.user3.username)

    def test_user_create_get(self):
        response = self.client.get(reverse_lazy('create'))

        self.assertTemplateUsed(response, template_name='registration.html')
        self.assertEqual(response.status_code, 200)

    def test_user_create_post(self):
        params = self.test_user
        params.update({'username': ''})
        response = self.client.post(reverse_lazy('create'), data=params)
        errors = response.context['form'].errors
        self.assertIn('username', errors)
        self.assertEqual(
            ['Обязательное поле.'],
            errors['username']
        )
        params.update({'username': 'Test1'})
        response = self.client.post(reverse_lazy('create'), data=params)
        self.assertTrue(User.objects.get(id=4))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

    def test_user_update_get(self):
        self.client.force_login(self.user1)
        response = self.client.get(
            reverse_lazy('user_update', args=[self.user1.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='registration.html')

    def test_user_update_without_auth(self):
        response = self.client.get(
            reverse_lazy('user_update', args=[self.user1.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

    def test_user_update_another_user(self):
        self.client.force_login(self.user2)
        response = self.client.get(
            reverse_lazy('user_update', args=[self.user1.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('users'))

    def test_user_update_post(self) -> None:
        params = self.test_user
        self.client.force_login(self.user1)
        response = self.client.post(
            reverse_lazy('user_update', args=[self.user1.id]),
            data=params
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('users'))

        updated_user = User.objects.get(id=self.user1.id)
        self.assertEqual(updated_user.username, params['username'])
        self.assertEqual(updated_user.first_name, params['first_name'])
        self.assertEqual(updated_user.last_name, params['last_name'])

    def test_user_delete_get(self):
        self.client.force_login(self.user1)
        response = self.client.get(
            reverse_lazy('user_delete', args=[self.user1.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='delete.html')

    def test_user_delete_post(self):
        before_objs_len = len(User.objects.all())
        self.client.force_login(self.user1)
        response = self.client.post(
            reverse_lazy('user_delete', args=[self.user1.id])
        )
        after_objs_len = len(User.objects.all())

        self.assertTrue(after_objs_len == before_objs_len - 1)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('users'))
