from django.test import TestCase
from .models import Projects, Profile
from django.contrib.auth.models import User

# Create your tests here.
class TestProfile(TestCase):
    def setUp(self):
        self.user = User(user='profile')
        self.user.save()

        self.prof = Profile(user=self.user, profile_pic="image", bio="Amaze", contact="123" )
        self.prof.save_profile()

    def test_instance(self):
        self.assertTrue(isinstance(self.prof,Profile))

    def tearDown(self):
        Profile.objects.all().delete()

    def test_delete_profile(self):
        self.prof.delete_image()
        image = Profile.objects.all()
        self.assertEqual(len(image), 0)


class TestProjects(TestCase):
    def setUp(self):
        self.user = User(profile="Profile")
        self.user.save()

        self.new_project = Projects(title="image", image="john", description="Amazing", live_link="http://example.com", posted_by=self.user)
        self.new_project.save_project()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_project, Projects))

    def tearDown(self):
        Projects.objects.all().delete()

    def test_delete_profile(self):
        self.new_project.delete_project()
        project = Projects.objects.all()
        self.assertEqual(len(project), 0)