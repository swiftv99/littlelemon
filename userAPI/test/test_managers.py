from rest_framework.test import APITestCase
from userAPI.models import User


class TestModel(APITestCase):
    
    def test_create_user(self):
        user = User.objects.create_user("cryce", "crycetruly@gmail.com", "Password@123")
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, "crycetruly@gmail.com")

    # def test_raising_error_when_no_username_is_supplied(self):
    #     self.assertRaises(ValueError, User.objects.create_user, username="", email="crycetruly@gmail.com", password="Password@123")
    
    def test_raising_error_message_when_no_username_is_supplied(self):
        with self.assertRaisesMessage(ValueError, "The Username field must be set"):
            User.objects.create_user(username="", email="crycetruly@gmail.com", password="Password@123")
 
    # def test_raising_error_when_no_email_is_supplied(self):
    #     self.assertRaises(ValueError, User.objects.create_user, username="cryce", email="", password="Password@123")        
             
    def test_raising_error_message_when_no_email_is_supplied(self):
        with self.assertRaisesMessage(ValueError, "The Email field must be set"):
            User.objects.create_user(username="cryce", email="", password="Password@123")

              
    def test_create_super_user(self):
        user = User.objects.create_superuser("cryce", "crycetruly@gmail.com", "Password@123")
        self.assertIsInstance(user, User)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email, "crycetruly@gmail.com")
  
  
    def test_create_superuser_with_staff_status(self):
        with self.assertRaisesMessage(ValueError, "Superuser must have is_staff=True."):
            User.objects.create_superuser(username="cryce", email="crycetruly@gmail.com", password="Password@123", is_staff=False)
            
            
    def test_create_superuser_with_superuser_status(self):
        with self.assertRaisesMessage(ValueError, "Superuser must have is_superuser=True."):
            User.objects.create_superuser(username="cryce", email="crycetruly@gmail.com", password="Password@123", is_superuser=False)
