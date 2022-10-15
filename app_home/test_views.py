""" Tests the home index.html view """
from django.test import TestCase

from app_properties.models import Property, Category


class TestHomeViews(TestCase):
    """ Tests the home app views """
    def setUp(self):
        self.category = Category.objects.create(
            name='test',
            friendly_name='Test Category'
        )

        self.page = Property.objects.create(
            category=self.category,
            name='Test Property',
            ribbon_feature='This is a test page',
            description='This is test New Property Entry',
            house_no=22,
            bedrooms=3,
            bathrooms=1,
            carports=1,
            air_conditioning=1
        )
        self.category.title_page = self.page
        self.category.save()

    def test_landing_page(self):
        """ Tests loading the landing page """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
