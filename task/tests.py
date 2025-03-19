from django.test import TestCase
from account.models import User
from project.models import Project
from todolist.models import Todolist
from task.models import Task

class TaskModelTests(TestCase):

    def setUp(self):
        # Set up a user
        self.user = User.objects.create_user(
            email='user@example.com',
            password='testpassword'
        )

        # Set up a project
        self.project = Project.objects.create(
            name='Test Project',
            created_by=self.user
        )

        # Set up a todolist
        self.todolist = Todolist.objects.create(
            name='Test Todolist',
            created_by=self.user
        )

    def test_create_task(self):
        # Test task creation with required fields
        task = Task.objects.create(
            project=self.project,
            Todolist=self.todolist,
            name='Test Task',
            description='Test Description',
            created_by=self.user
        )
        self.assertEqual(task.name, 'Test Task')
        self.assertEqual(task.description, 'Test Description')
        self.assertEqual(task.project, self.project)
        self.assertEqual(task.Todolist, self.todolist)
        self.assertEqual(task.created_by, self.user)
        self.assertFalse(task.is_done)  # Default is_done should be False

    def test_create_task_without_description(self):
        # Test task creation without a description
        task = Task.objects.create(
            project=self.project,
            Todolist=self.todolist,
            name='Test Task Without Description',
            created_by=self.user
        )
        self.assertEqual(task.name, 'Test Task Without Description')
        self.assertIsNone(task.description)  # description should be None as it is optional
        self.assertFalse(task.is_done)  # Default is_done should be False

    def test_task_is_done_default(self):
        # Test the default value of the 'is_done' field
        task = Task.objects.create(
            project=self.project,
            Todolist=self.todolist,
            name='Test Task for is_done Default',
            created_by=self.user
        )
        self.assertFalse(task.is_done)  # The default value should be False

    def test_task_string_representation(self):
        # Test the string representation of the task
        task = Task.objects.create(
            project=self.project,
            Todolist=self.todolist,
            name='Test Task String Representation',
            created_by=self.user
        )
        self.assertEqual(str(task), 'Test Task String Representation')

    def test_task_relationship_with_project(self):
        # Test if task is related to the project
        task = Task.objects.create(
            project=self.project,
            Todolist=self.todolist,
            name='Test Task Project Relationship',
            created_by=self.user
        )
        self.assertIn(task, self.project.tasks.all())  # Check if task is related to the project

    def test_task_relationship_with_todolist(self):
        # Test if task is related to the todolist
        task = Task.objects.create(
            project=self.project,
            Todolist=self.todolist,
            name='Test Task Todolist Relationship',
            created_by=self.user
        )
        self.assertIn(task, self.todolist.tasks.all())  # Check if task is related to the todolist

    def test_task_relationship_with_user(self):
        # Test if task is related to the user
        task = Task.objects.create(
            project=self.project,
            Todolist=self.todolist,
            name='Test Task User Relationship',
            created_by=self.user
        )
        self.assertIn(task, self.user.tasks.all())  # Check if task is related to the user
