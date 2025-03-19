from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

class CustomUserTests(TestCase):

    def test_create_user_with_email_and_password(self):
        # Creating a regular user with email and password
        user = get_user_model().objects.create_user(
            email='testuser@example.com',
            password='testpassword'
        )
        self.assertEqual(user.email, 'testuser@example.com')
        self.assertTrue(user.check_password('testpassword'))  # Checking if the password is hashed correctly
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_user_without_email(self):
        # Ensure a ValueError is raised if email is not provided
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None,
                password='testpassword'
            )

    def test_create_superuser(self):
        # Create a superuser and check if flags are set correctly
        superuser = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='testpassword',
            name='Admin'
        )
        self.assertEqual(superuser.email, 'admin@example.com')
        self.assertTrue(superuser.check_password('testpassword'))
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

    def test_create_user_with_name(self):
        # Creating user with name provided
        user = get_user_model().objects.create_user(
            email='testuserwithname@example.com',
            password='testpassword',
            name='John Doe'
        )
        self.assertEqual(user.name, 'John Doe')

    def test_create_user_without_name(self):
        # Creating user without providing name (optional)
        user = get_user_model().objects.create_user(
            email='testuserwithoutname@example.com',
            password='testpassword'
        )
        self.assertIsNone(user.name)  # name should be None as it's optional

    def test_user_password_is_hashed(self):
        # Ensure password is hashed and not stored in plain text
        user = get_user_model().objects.create_user(
            email='passwordcheck@example.com',
            password='testpassword'
        )
        self.assertNotEqual(user.password, 'testpassword')  # The stored password should not match the plain text password

    def test_create_user_with_invalid_email(self):
        # Ensure a ValueError is raised when an invalid email is provided
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email='invalid-email',
                password='testpassword'
            )

    def test_user_unique_email(self):
        # Ensure that emails are unique in the database
        get_user_model().objects.create_user(
            email='duplicate@example.com',
            password='testpassword'
        )
        with self.assertRaises(ValidationError):
            get_user_model().objects.create_user(
                email='duplicate@example.com',
                password='newpassword'
            )
