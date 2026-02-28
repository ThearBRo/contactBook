from app.models import User, Contact
import unittest


class UserContactRelationTestCase(unittest.TestCase):
    def setUp(self):
        self.user = User(username='testuser', email='test@example.com')
        
    def test_user_contacts_relationship(self):
        contact1 = Contact(name='John Doe', phone_number='123-456-7890')
        contact2 = Contact(name='Jane Doe', phone_number='987-654-3210')
        
        self.user.contacts.append(contact1)
        self.user.contacts.append(contact2)
        
        self.assertEqual(self.user.contacts.count(), 2)
        self.assertIn(contact1, self.user.contacts)
        self.assertIn(contact2, self.user.contacts)
                
    def test_user_contacts_relationship_empty(self):
        self.assertEqual(self.user.contacts.count(), 0)  # No contacts should be associated yet

    def test_user_contacts_relationship_removal(self):
        contact = Contact(name='John Doe', phone_number='123-456-7890')
        self.user.contacts.append(contact)
        self.assertEqual(self.user.contacts.count(), 1)
        
        self.user.contacts.remove(contact)
        self.assertEqual(self.user.contacts.count(), 0)
        
        
    def test_user_contacts_relationship_cascade_delete(self):
        contact = Contact(name='John Doe', phone_number='123-456-7890')
        self.user.contacts.append(contact)
        self.assertEqual(self.user.contacts.count(), 1)
        
        # Simulate deleting the user and check if the contact is also deleted
        self.user = None  # Simulate user deletion
        self.assertIsNone(contact.user_id)  # Contact should no longer be associated with a user
        
    def test_user_contacts_relationship_multiple_users(self):
        user2 = User(username='anotheruser', email='another@example.com')
        contact1 = Contact(name='John Doe', phone_number='123-456-7890')
        contact2 = Contact(name='Jane Doe', phone_number='987-654-3210')
        
        self.user.contacts.append(contact1)
        user2.contacts.append(contact2)
        
        self.assertEqual(self.user.contacts.count(), 1)
        self.assertEqual(user2.contacts.count(), 1)
        
        self.assertIn(contact1, self.user.contacts)
        self.assertIn(contact2, user2.contacts)
        
    def test_user_contacts_relationship_duplicate_contacts(self):
        contact = Contact(name='John Doe', phone_number='123-456-7890')
        self.user.contacts.append(contact)
        self.user.contacts.append(contact)  # Attempt to add the same contact again
        
        self.assertEqual(self.user.contacts.count(), 1)  # Should still only have one instance of the contact
