from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from unittest import skip

from content.views import home_page

# Create your tests here.
class HomeTest(TestCase):
    def load_html(self):
        request = HttpRequest()
        return home_page(request).content.decode('utf-8')

    def test_base_url_routes(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_has_html(self):
        self.assertIn("<html>", self.load_html())

    def test_use_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_have_upload_id(self):
        self.assertIn("id_upload", self.load_html())

    def test_saves_POST_request(self):
        response = self.client.post('/', data={'upload_text': 'A link probably'})
        self.assertIn('A link probably', response.content.decode())

    def test_form_POSTS(self):
        self.assertIn('method="POST"', self.load_html())
