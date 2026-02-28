import unittest
from app.models import Contact

class ContactModelTestCase(unittest.TestCase):
    def setUp(self):
        self.contact = Contact(name='John Doe', phone_number='123-456-7890')
        
    def test_contact_representation(self):
        self.assertEqual(repr(self.contact), '<Contact John Doe>')
        
    def test_contact_fields(self):
        self.assertEqual(self.contact.name, 'John Doe')
        self.assertEqual(self.contact.phone_number, '123-456-7890')
        
    def test_contact_id(self):
        self.assertIsNone(self.contact.id)  # ID should be None before being added to the database
        
    def test_contact_user_id(self):
        self.assertIsNone(self.contact.user_id)  # user_id should be None before being associated with a user    
    
    def test_contact_to_string(self):
        self.assertEqual(str(self.contact), '<Contact John Doe>')

    def test_contact_phone_number_optional(self):
        contact = Contact(name='Jane Doe')  # phone_number is optional
        self.assertEqual(contact.name, 'Jane Doe')
        self.assertIsNone(contact.phone_number)

    def test_contact_info_method(self):
        self.assertEqual(self.contact.contact_info(), 'Name: John Doe, Phone: 123-456-7890')
        contact_without_phone = Contact(name='Jane Doe')
        self.assertEqual(contact_without_phone.contact_info(), 'Name: Jane Doe, Phone: N/A')
        
    
if __name__ == '__main__':
    unittest.main()