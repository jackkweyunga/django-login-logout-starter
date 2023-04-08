from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class UserModelTestCase(TestCase):
    def setUp(self):
        self.User = get_user_model()
        self.user_data = {
            "email": "test@example.com",
            "username": "testusername",
            "first_name": "John",
            "last_name": "Doe",
            "phone_number": "1234567890",
            "profile_pic_url": "https://example.com/test.jpg",
        }
        self.super_user_data = {
            "email": "supertest@example.com",
            "username": "supertestusername",
            "phone_number": "3235",
            "profile_pic_url": "https://example.com/test.jpg",
        }
        self.user = self.User.objects.create_user(
            **self.user_data, password="testpassword"
        )

    def test_create_user(self):
        user = self.user
        self.assertEqual(user.email, self.user_data["email"])
        self.assertEqual(user.phone_number, self.user_data["phone_number"])
        self.assertEqual(user.username, self.user_data["username"])
        self.assertEqual(user.profile_pic_url, self.user_data["profile_pic_url"])
        self.assertTrue(user.check_password("testpassword"))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        superuser = self.User.objects.create_superuser(
            **self.super_user_data, password="testpassword"
        )
        self.assertEqual(superuser.email, self.super_user_data["email"])
        self.assertEqual(superuser.phone_number, self.super_user_data["phone_number"])
        self.assertEqual(
            superuser.profile_pic_url, self.super_user_data["profile_pic_url"]
        )
        self.assertTrue(superuser.check_password("testpassword"))
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

    def test_get_absolute_url(self):
        url = self.user.get_absolute_url()
        expected_url = self.user.get_detail_url()
        self.assertEqual(url, expected_url)

    def test_get_detail_url(self):
        url = self.user.get_detail_url()
        expected_url = reverse("users:user-detail", kwargs={"pk": self.user.pk})
        self.assertEqual(url, expected_url)

    def test_get_update_url(self):
        url = self.user.get_update_url()
        expected_url = reverse("users:user-update", kwargs={"pk": self.user.pk})
        self.assertEqual(url, expected_url)

    def test_get_list_url(self):
        url = self.user.get_list_url()
        expected_url = reverse("users:user-list")
        self.assertEqual(url, expected_url)

    def test_get_success_url(self):
        url = self.user.get_success_url()
        expected_url = self.user.get_detail_url()
        self.assertEqual(url, expected_url)

    def test_default_profile_pic_url(self):
        expected_url = (
            "https://eu.ui-avatars.com/api/"
            "?name=John+Doe&size=250&background=0D8ABC&color=fff&"
        )
        self.assertEqual(self.user.default_profile_pic_url, expected_url)

    def test_default_username(self):
        self.assertEqual(self.user.default_username, "test")

    def test_name(self):
        self.assertEqual(self.user.name, "John Doe")
