"""
This script runs the application using a development server.
"""

from datetime import datetime
import bottle
import os
import sys
from addEvent import load_events
from addPartners import load_partners

events = {}
partners = {}
# routes contains the HTTP handlers for our server and must be imported.
import routes

# @bottle.route('/events')
# def load_events_list():
#     events = addEvent.json_to_list()
#     return bottle.template('events', events=events)

if '--debug' in sys.argv[1:] or 'SERVER_DEBUG' in os.environ:
    # Debug mode will enable more verbose output in the console window.
    # It must be set at the beginning of the script.
    bottle.debug(True)

def wsgi_app():
    """Returns the application to make available through wfastcgi. This is used
    when the site is published to Microsoft Azure."""
    return bottle.default_app()

if __name__ == '__main__':
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static').replace('\\', '/')
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    
    @bottle.route('/static/<filepath:path>')
    def server_static(filepath):
        """Handler for static files, used with the development server.
        When running under a production server such as IIS or Apache,
        the server should be configured to serve the static files."""
        return bottle.static_file(filepath, root=STATIC_ROOT)

    bottle.route('/events', ['GET', 'POST'], load_events,title="Events",year=datetime.now().year)
    bottle.route('/partners', ['GET', 'POST'], load_partners,title="Partners",year=datetime.now().year)
    # Starts a local test server.
    bottle.run(server='wsgiref', host=HOST, port=PORT)