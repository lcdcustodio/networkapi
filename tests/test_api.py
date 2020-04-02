
from django.test import SimpleTestCase, TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status

from rest_framework.test import APIRequestFactory
from core.views import IpAddressViewSet

#User = get_user_model()


class TestApi(TestCase):

    def setUp(self):
        """
        User.objects.create_superuser(username='admin',
                                      password='tester',
                                      email='admin@admin.com')
        self.client.login(username='admin', password='tester')
        """
        #self.factory = APIRequestFactory()

        #request = self.factory.post('/notes/', {'title': 'new idea'}, format='json')
        #response = view(request)

        #request = self.factory.get('/accounts/django-superstars/')
        #print("lala")
        #print(request)

        #self.assertEqual(request, {'id': 4, 'username': 'lauren'})
        #url = reverse('api:IpAddress-list')
        #self.url1 = True
        #assert True == self.url1
        #request = self.factory.get('/accounts/django-superstars/')
        #print (request)
        #self.assertEqual(request.data, {'id': 4, 'username': 'lauren'})
        #url = reverse('api:network-list')

    def test_get_api(self):

        url = reverse('api:network-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])


    def test_post_api(self):

        url = reverse('api:network-new')
        payload = {'ip_address': '1.1.1.2', 'subnet':'1.1.1.0/24'}

        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['status'], 'success')

    def test_delete_api(self):

        url = reverse('api:network-new')
        payload = {'ip_address': '1.1.1.117', 'subnet':'1.1.1.0/24'}

        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['status'], 'success')

        url = reverse('api:network-detail', kwargs={'pk': response.data['info']['id']})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['status'], 'delete successful')

