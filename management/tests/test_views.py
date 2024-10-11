from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from ..models import Equipment  


class EquipmentTests(APITestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username='testuser1', password='password1')

        self.token = Token.objects.create(user=self.user)

        self.equipment_data = {
            'name': 'First Resturant',
            'price': 200.99,
            'flag': True
        }
        self.equipment = Equipment.objects.create(**self.equipment_data)

    def test_get_equipment_authenticated(self):

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get(reverse('equipment-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1) 

    def test_get_equipment_unauthenticated(self):

        response = self.client.get(reverse('equipment-list'))
        self.assertEqual(response.status_code,
                         status.HTTP_403_FORBIDDEN)  
