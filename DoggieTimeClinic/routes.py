"""
Routes and views for the bottle application.
"""

from tempfile import template
from bottle import route, view
from datetime import datetime
from active import is_valid_email, is_valid_phone, load_questions, request, save_question

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )

@route('/contact')
@view('contact')
def contact():
    """Renders the contact page."""
    return dict(
        title='Contact',
        message='Your contact page.',
        year=datetime.now().year
    )

@route('/about')
@view('about')
def about():
    """Renders the about page."""
    return dict(
        title='About',
        message='Your application description page.',
        year=datetime.now().year
    )

@route('/events')
@view('events')
def usefulText():
    """Renders the events page."""
    return dict(
        title='Events',
        message='Old and new events right here',
        year=datetime.now().year
    )

@route('/partners')
@view('partners')
def usefulText():
    """Renders the partners page."""
    return dict(
        title='Partners',
        message='Our partners right here',
        year=datetime.now().year
    )

@route('/active', method=['GET', 'POST'])
@view('active')
def active():
    errors = {}
    name = request.forms.get('name', '').strip()
    email = request.forms.get('email', '').strip()
    phone = request.forms.get('phone', '').strip()
    question = request.forms.get('question', '').strip()

    if request.method == 'POST':
        if not name: 
            errors['name'] = "Name required"
        if not is_valid_email(email): 
            errors['email'] = "Invalid email"
        if not is_valid_phone(phone): 
            errors['phone'] = "Invalid phone"
        if not question: 
            errors['question'] = "Question required"

        if not errors:
            save_question(name, email, phone, question)

    questions = load_questions()
    return dict(
        name=name,
        email=email,
        phone=phone,
        question=question,
        errors=errors,
        questions=questions
    )
   