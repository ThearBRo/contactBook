from app.services import UserService, ContactService
from flask import Blueprint, request, render_template, redirect, url_for, flash
from app.forms import UserForm, EditUserForm, LoginForm
from flask_login import login_user, logout_user, login_required, current_user

user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/users', methods=['GET'])
def list_users():
    users = UserService.get_all_users()
    return render_template('users.html', users=users)


@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = UserForm()
    if form.validate_on_submit():
        user = UserService.create_user(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data
        )
        flash('Account created. You can now log in.', 'success')
        return redirect(url_for('user_bp.login'))
    return render_template('auth/register.html', form=form)


@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = UserService.get_user_by_username(form.email.data) or UserService.get_user_by_username(form.email.data)
        # The project uses email as login in forms; attempt to find by email
        from app.models.user_model import User
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.verify_password(form.password.data):
            login_user(user)
            flash('Welcome back!', 'success')
            return redirect(url_for('contact_bp.contacts'))
        flash('Invalid credentials', 'danger')
    return render_template('auth/login.html', form=form)


@user_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('user_bp.login'))
