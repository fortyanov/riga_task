from django.test import TestCase

from main.bl import NumberHandler, TextHandler
from main.models import UsefulNumber, UsefulText


class NumberHandlerTestCase(TestCase):
    def setUp(self):
        for i in range(1, 10):
            UsefulNumber.objects.create(number=i)

    def test_number_handler(self):
        bl_result = NumberHandler({'number': 100}).run()

        self.assertEqual(bl_result, {'Average number': 14.5})
        self.assertEqual(UsefulNumber.objects.count(), 10)


class TextHandlerTestCase(TestCase):
    def setUp(self):
        UsefulText.objects.create(text='hello')

    def test_text_handler(self):
        bl_result = TextHandler({'text': 'world'}).run()

        self.assertEqual(bl_result, {'Concatenated text': 'hello SPAM world'})
        self.assertEqual(UsefulText.objects.count(), 2)
