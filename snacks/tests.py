from django.http import response
from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.


class SnacksTests(SimpleTestCase):
    def test_home_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_about_us_status_code(self):
        url = reverse('about-us')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
    def test_home_page_template(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, "home.html")
        self.assertTemplateUsed(response, "_base.html")

    def test_about_us_page_template(self):
        url = reverse('about-us')
        response = self.client.get(url)
        self.assertTemplateUsed(response, "about_us.html")
        self.assertTemplateUsed(response, "_base.html")
