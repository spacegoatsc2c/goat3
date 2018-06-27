from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from unittest import skip

from content.views import home_page
from content.models import Content

# Create your tests here.
class HomeViewTest(TestCase):
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

    def test_saves_multiple_POST_requests(self):
        self.client.post('/', data={'upload_text': 'First'})
        response = self.client.post('/', data={'upload_text': 'Second'})
        self.assertIn('First', response.content.decode())
        self.assertIn('Second', response.content.decode())

class ContentModelTest(TestCase):

    def test_saving_and_retreiving(self):
        content = Content.objects.create(text="First Content")
        self.assertEqual(content, Content.objects.first())
        self.assertEqual(content.text, Content.objects.first().text)

    def test_saving_multiple(self):
        first_content = Content.objects.create(text="First")
        second_content = Content.objects.create(text="Second")
        self.assertIn(first_content, list(Content.objects.all()))
        self.assertIn(second_content, list(Content.objects.all()))
