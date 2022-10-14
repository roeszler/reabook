""" Import Modules """
from django.test import TestCase
from .views import integer_type_check


class TestTypeInteger(TestCase):
    """ To test the integer_type_check function in working """
    
    def test_entry_is_integer(self):
        """ To test that input is an integer """
        self.assertIsInstance(integer_type_check(233), int)

    # def test_entry_is_integer(self):
    #     """ To test that input is exactly equal to 10 """
    #     self.assertEqual(integer_type_check(10), True)
    
    # def test_entry_is_integer(self):
    #     """ To test that input is not a string """
    #     self.assertIsInstance(integer_type_check('233'), int)
    
    # def test_entry_is_integer(self):
    #     """ To test that input is not a float """
    #     self.assertIsInstance(integer_type_check(233.3), int)
    
    # def test_entry_is_integer(self):
    #     """ No more than one input required """
    #     self.assertIsInstance(integer_type_check(21, 22), int)


class TestDjango(TestCase):
    """ To test unittest.TestCase is functioning """

    def test_test_case_works(self):
        """ To test... """
        self.assertEqual(1, 1)

    # def test_test_case_works(self):
    #     self.assertEqual(1, 2)

    # def test_test_case_works(self):
    #     self.assertEqual(1, )

    # def test_test_case_works(self):
    #     self.assertEqual(1, 5)