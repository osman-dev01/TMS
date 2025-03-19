from django.test import TestCase
from account.models import User
from project.models import Project
from todolist.models import Todolist

class TodolistModelTests(TestCase):

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

    def test_create_todolist(self):
        # Test todolist creation with required fields
        todolist = Todolist.objects.create(
            project=self.project,
            name='Test Todolist',
            description='Test Description',
            created_by=self.user
        )
        self.assertEqual(todolist.name, 'Test Todolist')
        self.assertEqual(todolist.description, 'Test Description')
        self.assertEqual(todolist.project, self.project)
        self.assertEqual(todolist.created_by, self.user)

    def test_create_todolist_without_description(self):
        # Test todolist creation without a description
        todolist = Todolist.objects.create(
            project=self.project,
            name='Test Todolist Without Description',
            created_by=self.user
        )
        self.assertEqual(todolist.name, 'Test Todolist Without Description')
        self.assertIsNone(todolist.description)  # description should be None as it is optional

    def test_todolist_string_representation(self):
        # Test the string representation of the todolist
        todolist = Todolist.objects.create(
            project=self.project,
            name='Test Todolist String Representation',
            created_by=self.user
        )
        self.assertEqual(str(todolist), 'Test Todolist String Representation')

    def test_todolist_relationship_with_project(self):
        # Test if todolist is related to the project
        todolist = Todolist.objects.create(
            project=self.project,
            name='Test Todolist Project Relationship',
            created_by=self.user
        )
        self.assertIn(todolist, self.project.todolists.all())  # Check if todolist is related to the project

    def test_todolist_relationship_with_user(self):
        # Test if todolist is related to the user
        todolist = Todolist.objects.create(
            project=self.project,
            name='Test Todolist User Relationship',
            created_by=self.user
        )
        self.assertIn(todolist, self.user.todolists.all())  # Check if todolist is related to the user
