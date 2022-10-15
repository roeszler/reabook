""" Import Modules """
from django.test import TestCase


class TestDjango(TestCase):
    """ To ensure django test function working in app """

    def test_test_case_works(self):
        """ To ensure django test function working in app """
        self.assertEqual(1, 1)
