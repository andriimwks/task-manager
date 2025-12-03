from django.test import TestCase
from django.utils import timezone
from django.contrib.auth import get_user_model
from ..models import Project, Task


User = get_user_model()


class TaskModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="test@test.com", password="1sJ!789?")
        self.project = Project.objects.create(name="Test", created_by=self.user)

    def test_is_overdue(self):
        task = Task.objects.create(
            project=self.project,
            name="Test",
            deadline=timezone.now().date() - timezone.timedelta(days=1),
        )
        self.assertTrue(task.is_overdue())

    def test_is_not_overdue_if_completed(self):
        task = Task.objects.create(
            project=self.project,
            name="Test",
            deadline=timezone.now().date() - timezone.timedelta(days=1),
            completed=True,
        )
        self.assertFalse(task.is_overdue())

    def test_days_remaining(self):
        task = Task.objects.create(
            project=self.project,
            name="Test",
            deadline=timezone.now().date() + timezone.timedelta(days=5),
        )
        self.assertEqual(task.days_remaining(), 5)
