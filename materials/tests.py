from django.test import TestCase
from .models import Material


class MaterialModel(TestCase):
    def test_name(self):
        material = Material(title='First material')
        self.assertIs(material.title, 'First material')

    def test_default_fields(self):
        material = Material(title='Material')
        self.assertEqual(material.title, 'Material')
        self.assertEqual(material.description, 'material description')
        self.assertEqual(material.content, 'material content')
