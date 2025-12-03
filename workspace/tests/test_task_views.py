from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from ..models import Project, Task


User = get_user_model()


class TaskViewsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="test@test.com", password="1sJ!789?")
        self.client.login(email="test@test.com", password="1sJ!789?")
        self.project = Project.objects.create(name="Test", created_by=self.user)
        self.task = Task.objects.create(name="Test Task", project=self.project)

    #
    # Create task
    #

    def test_create_task_valid(self):
        response = self.client.post(
            reverse("workspace:create_task", args=[self.project.pk]),
            {"name": "Test Task 2"},
            HTTP_HX_REQUEST="true",
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(name="Test Task 2").exists())

    def test_create_task_invalid(self):
        response = self.client.post(
            reverse("workspace:create_task", args=[self.project.pk]),
            {"name": ""},
            HTTP_HX_REQUEST="true",
        )
        self.assertEqual(response.status_code, 400)

    #
    # Update task
    #

    def test_update_task_valid(self):
        response = self.client.post(
            reverse("workspace:update_task", args=[self.task.pk]),
            {
                "name": "Updated Task",
                "priority": Task.Priorities.HIGH,
                "deadline": "",
                "completed": False,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertEqual(self.task.name, "Updated Task")
        self.assertEqual(self.task.priority, Task.Priorities.HIGH)

    def test_update_task_invalid(self):
        response = self.client.post(
            reverse("workspace:update_task", args=[self.task.pk]),
            {"name": ""},
        )
        self.assertEqual(response.status_code, 400)

    #
    # Complete task
    #

    def test_complete_task(self):
        response = self.client.post(
            reverse("workspace:complete_task", args=[self.task.pk]),
            {"completed": True},
            HTTP_HX_REQUEST="true",
        )
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertTrue(self.task.completed)

    #
    # Delete task
    #

    def test_delete_task(self):
        response = self.client.delete(
            reverse("workspace:delete_task", args=[self.task.pk]),
            HTTP_HX_REQUEST="true",
        )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())
