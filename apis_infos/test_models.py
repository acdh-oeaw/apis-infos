from faker import Faker
from django.test import TestCase
from .models import ProjectInst

fake = Faker()


class ProjectInstTestCase(TestCase):
    def setUp(self):
        self.inst1name = fake.name()
        self.inst2name = fake.name()
        ProjectInst.objects.create(name=self.inst1name)
        ProjectInst.objects.create(name=self.inst2name)

    def test_project(self):
        p1 = ProjectInst.objects.get(name=self.inst1name)
        p2 = ProjectInst.objects.get(name=self.inst2name)
        self.assertEqual(str(p1), self.inst1name)
        self.assertEqual(str(p2), self.inst2name)
