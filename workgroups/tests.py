from django.test import TestCase
from .models import Workgroup


class WorkgroupModel(TestCase):
    def test_name(self):
        workgroup = Workgroup(name='First Workgroup')
        self.assertIs(workgroup.name, 'First Workgroup')

    def test_default_fields(self):
        workgroup = Workgroup(name='Workgroup')
        self.assertEqual(workgroup.name, 'Workgroup')
        self.assertEqual(workgroup.topic, 'workgroup topic')
        self.assertEqual(workgroup.supervisor, 'workgroup supervisor')
        self.assertIs(workgroup.number_of_participants, 0)
