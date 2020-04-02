
from django.test import TestCase
from rest_framework.reverse import reverse


class TestApi(TestCase):


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

