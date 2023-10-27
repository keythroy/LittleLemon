from django.test import TestCase, Client
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.contrib.auth.models import User


class MenuViewTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

        Menu.objects.create(Title="IceCream", Price=40, Inventory=100)
        Menu.objects.create(Title="Coffe", Price=2, Inventory=100)
        Menu.objects.create(Title="Sandwich", Price=30, Inventory=100)

        self.path = "/api/menu-items/"

    def test_unathenticated_user(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, 401)

    def user_login(self):
        user = User.objects.create_user(username="test", password="test")
        self.client.login(username="test", password="test")

    def user_logout(self):
        self.client.logout()

    def test_get_menu_items(self):
        self.user_login()

        response = self.client.get(self.path)
        self.assertEqual(response.status_code, 200)

        expected = MenuSerializer(Menu.objects.all(),many=True)
        self.assertEqual(response.data, expected.data)
        
        self.user_logout()
