import unittest
from app.models import User

class UserModelTestCase(unittest.TestCase):
    def setUp(self):
        self.user = User(username='testuser', email='test@example.com')
        
    def test_password_hashing(self):
        self.user.password = 'password123'
        self.assertTrue(self.user.verify_password('password123'))
        self.assertFalse(self.user.verify_password('wrongpassword'))
        
    def test_password_not_readable(self):
        self.user.password = 'password123'
        with self.assertRaises(AttributeError):
            _ = self.user.password
            
    def test_user_representation(self):
        self.assertEqual(repr(self.user), '<User testuser>')
        
    def test_user_fields(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'test@example.com')
        
    def test_user_id(self):
        self.assertIsNone(self.user.id)  # ID should be None before being added to the database
        
    def test_user_contacts_relationship(self):
        self.assertEqual(self.user.contacts.count(), 0)  # No contacts should be associated yet
    
    def test_user_to_string(self):
        self.assertEqual(str(self.user), '<User testuser>')
        
    def test_user_password_hashing_consistency(self):
        self.user.password = 'password123'
        hash1 = self.user.password_hash
        self.user.password = 'password123'
        hash2 = self.user.password_hash
        self.assertNotEqual(hash1, hash2)  # Hashes should be different due to salting
        
    def test_user_password_verification_with_different_passwords(self):
        self.user.password = 'password123'
        self.assertFalse(self.user.verify_password('differentpassword'))
        
    def test_user_password_verification_with_empty_password(self):
        self.user.password = 'password123'
        self.assertFalse(self.user.verify_password(''))
    
    
if __name__ == '__main__':
    unittest.main()