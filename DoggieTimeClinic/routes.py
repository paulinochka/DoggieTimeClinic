"""
Routes and views for the bottle application.
"""

from bottle import route, view
from datetime import datetime

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
        title='events',
        message='Old and new events right here',
        year=datetime.now().year
    )

@route('/partners')
@view('partners')
def usefulText():
    """Renders the partners page."""
    return dict(
        title='partners',
        message='Our partners right here',
        year=datetime.now().year
    )

@route('/active')
@view('active')
def usefulText():
    """Renders the active page."""
    return dict(
        title='active',
        message='Yours active right here',
        year=datetime.now().year
    )