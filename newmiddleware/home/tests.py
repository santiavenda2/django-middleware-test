from django.test import TestCase
from django.urls import reverse


class HomeViewTests(TestCase):

    def test_index_view(self):

        response = self.client.get(reverse('home:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello, world. You're at the home index.")

    def test_index_view_without_slash(self):
        response = self.client.get('/home')
        self.assertEqual(response.status_code, 301)
