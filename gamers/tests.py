from django.test import TestCase
from rest_framework.test import APIRequestFactory
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from .models import Gamer
from rest_framework import status
import json

# Create your tests here.


factory = APIRequestFactory()
request = factory.post('/api/v1/gamers/', {'mobile': '11', 'score':'20'})

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_gamer(mobile, score):
        if mobile != "" and score != "":
            Gamer.objects.create(mobile=mobile, score=score)

    def setUp(self):
        self.create_gamer("11", 11)
        self.create_gamer("12", 12)
        self.create_gamer("13", 13)


# Testing creating object
class createGamer(BaseViewTest):
    def test_create_gamer(self):
        response = self.client.post('/api/v1/gamers/', {'mobile': '43', 'score': '20'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

# Testing indexing all objects
class GetAllGamers(BaseViewTest):
    def test_get_all_gamers(self):
        response = self.client.get('/api/v1/gamers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Gamer.objects.count(), 3)

# Testing getting one object rank
class CheckGamerScore(BaseViewTest):
    def test_gamer_score(self):
        response = self.client.get('/api/v1/gamers/11/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['rank'], 3)

# Testing updating object
class checkUpdateGamer(BaseViewTest):
    def test_update_gamer(self):
        response = self.client.put('/api/v1/gamers/11/', {'mobile': '11', 'score': '20'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(json.loads(response.content)['rank'], 1)

# Testing deleting object
class checkDeleteGamer(BaseViewTest):
    def test_delete_gamer(self):
        response = self.client.delete('/api/v1/gamers/11/')
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(Gamer.objects.count(), 2)
        
        