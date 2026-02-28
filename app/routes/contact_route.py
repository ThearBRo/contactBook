from app.services import ContactService
from flask import Blueprint, request, render_template, jsonify, redirect, url_for, flash
from app.forms.contact_form import ContactForm
from flask_login import login_required, current_user

contact_bp = Blueprint('contact_bp', __name__)


@contact_bp.route('/')
def home():
    return redirect(url_for('contact_bp.contacts'))


@contact_bp.route('/contacts', methods=['GET'])
@login_required
def contacts():
    contacts = ContactService.get_all_contacts()
    form = ContactForm()
    return render_template('contacts.html', contacts=contacts, form=form)


@contact_bp.route('/contacts', methods=['POST'])
@login_required
def create_contact():
    form = ContactForm()
    if form.validate_on_submit():
        ContactService.create_contact(name=form.name.data, phone_number=form.phone_number.data, user_id=current_user.id)
        flash('Contact created', 'success')
    else:
        flash('Invalid contact data', 'danger')
    return redirect(url_for('contact_bp.contacts'))


@contact_bp.route('/contacts/reorder', methods=['POST'])
@login_required
def reorder_contacts():
    # Accepts JSON array of contact ids in new order. We don't persist order in models,
    # but return success to allow client-side animations and feedback.
    data = request.get_json() or {}
    order = data.get('order')
    if not order:
        return jsonify({'status': 'error', 'message': 'No order provided'}), 400
    # In a future change we could persist positions; for now acknowledge.
    return jsonify({'status': 'ok'})
