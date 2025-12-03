from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from ..models import Project


User = get_user_model()


class ProjectViewsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="test@test.com", password="1sJ!789?")
        self.client.login(email="test@test.com", password="1sJ!789?")
        self.project = Project.objects.create(name="Test", created_by=self.user)

    #
    # Create project
    #

    def test_create_project(self):
        response = self.client.post(
            reverse("workspace:create_project"), {"name": "Test"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Project.objects.filter(name="Test").exists())

    #
    # Update project
    #

    def test_update_project_valid(self):
        response = self.client.post(
            reverse("workspace:update_project", args=[self.project.pk]),
            {"name": "Updated Name"},
            HTTP_HX_REQUEST="true",
        )
        self.assertEqual(response.status_code, 200)
        self.project.refresh_from_db()
        self.assertEqual(self.project.name, "Updated Name")

    def test_update_project_invalid(self):
        response = self.client.post(
            reverse("workspace:update_project", args=[self.project.pk]),
            {"name": ""},
            HTTP_HX_REQUEST="true",
        )
        self.assertEqual(response.status_code, 400)

    #
    # Delete project
    #

    def test_delete_project(self):
        response = self.client.delete(
            reverse("workspace:delete_project", args=[self.project.pk]),
            HTTP_HX_REQUEST="true",
        )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Project.objects.filter(id=self.project.pk).exists())
