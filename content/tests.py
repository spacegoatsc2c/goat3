from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.core.exceptions import ValidationError
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

    def test_do_not_save_duplicates(self):
        self.client.post('/', data={'upload_text': 'veryuniquishtext'})
        response = self.client.post('/', data={'upload_text': 'veryuniquishtext'})
        self.assertEqual(1, response.content.decode().count('veryuniquishtext'))
        self.assertTemplateUsed(response, 'home.html')

    def test_error_message_on_duplicates(self):
        self.client.post('/', data={'upload_text': 'an item'})
        response = self.client.post('/', data={'upload_text': 'an item'})
        self.assertIn("This has already been uploaded",
                response.content.decode()
        )
        self.assertTemplateUsed(response, 'home.html')

class ContentModelTest(TestCase):

    def test_saving_and_retreiving(self):
        content = Content.objects.create(text="First Content")
        self.assertEqual(content, Content.objects.first())
        self.assertEqual(content.text, Content.objects.first().text)

        second_content = Content.objects.create(text="Second")
        self.assertIn(second_content, list(Content.objects.all()))

    def test_duplicates_raise_exception(self):
        c = Content.objects.create(text="First")
        with self.assertRaises(ValidationError):
            c2 = Content(text="First")
            c2.save()
            c2.full_clean()
