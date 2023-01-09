from django.test import TestCase
from .models import Profiles
from django.contrib.auth.models import User


# Es nos permite crear prubas unitarias del codigo nos crea una base daos temporal que
# al final destruye lo que sea echo sin afectar a la base original
# Create your tests here.
class ProfileTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('test', 'test@gmail.com', 'test1234')

    def test_profile_exists(self):
        exists = Profiles.objects.filter(user_username='test').exists()
        self.assertEqual(exists, True)