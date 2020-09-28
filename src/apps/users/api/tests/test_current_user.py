from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from src.apps.users.tests.factories.user import UserFactory


class CurrentUserTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = UserFactory()
        self.client.force_login(self.user)

    def test(self):
        response = self.client.get(
            path=reverse('users:current')
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                'id': self.user.id,
                'username': self.user.username,
                'email': self.user.email,
                'first_name': self.user.first_name,
                'last_name': self.user.last_name,
            }
        )
