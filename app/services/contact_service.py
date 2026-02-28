from app import db
from app.models import Contact



class ContactService:
    @staticmethod
    def create_contact(name, phone_number, user_id):
        contact = Contact(name=name, phone_number=phone_number, user_id=user_id)
        db.session.add(contact)
        db.session.commit()
        return contact

    @staticmethod
    def get_contact_by_id(contact_id):
        return Contact.query.get(contact_id)

    @staticmethod
    def update_contact(contact_id, **kwargs):
        contact = Contact.query.get(contact_id)
        if not contact:
            return None
        for key, value in kwargs.items():
            setattr(contact, key, value)
        db.session.commit()
        return contact

    @staticmethod
    def delete_contact(contact_id):
        contact = Contact.query.get(contact_id)
        if not contact:
            return False
        db.session.delete(contact)
        db.session.commit()
        return True
    
    @staticmethod
    def get_all_contacts():
        return Contact.query.all()
    
    @staticmethod
    def search_contacts_by_name(name):
        return Contact.query.filter(Contact.name.ilike(f'%{name}%')).all()
    
    @staticmethod
    def search_contacts_by_phone_number(phone_number):
        return Contact.query.filter(Contact.phone_number.ilike(f'%{phone_number}%')).all()
    
    @staticmethod
    def get_contacts_paginated(page, per_page):
        return Contact.query.paginate(page=page, per_page=per_page, error_out=False)