from django.test import TestCase
from django.contrib.auth import get_user_model
from project.models import Project

class ProjectModelTests(TestCase):

    def test_project_creation(self):
        # Create a user with a valid email address and no 'username' (if your custom model uses 'email' instead of 'username')
        user = get_user_model().objects.create_user(
            email='testuser@example.com',  # Use email instead of username if it's your custom model
            password='testpassword'
        )
        
        # Create a project linked to the user
        project = Project.objects.create(
            name='Test Project',
            created_by=user  # Assigning the user to the 'created_by' field
        )
        
        # Check if the project is created successfully
        self.assertEqual(project.name, 'Test Project')
        self.assertEqual(project.created_by.email, 'testuser@example.com')  # Checking email as per custom model

    def test_project_creation_without_user(self):
        # Ensure that the 'created_by' field is required
        with self.assertRaises(ValueError):
            Project.objects.create(
                name='Test Project Without User',
                # Omitting the 'created_by' field to simulate a missing user
            )
