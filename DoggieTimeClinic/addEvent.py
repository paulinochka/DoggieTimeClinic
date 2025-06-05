from datetime import datetime
from os import error
from addPartners import NULL
from bottle import route, template, post, request
import json
import re
from pathlib import Path

error_message = ""
path = Path('static/otherFiles/events.json') 
def update_json(title,organiser,phone,description):
    try:
        events = json.loads(path.read_text(encoding='utf-8'))
    except (FileNotFoundError, json.JSONDecodeError):
        events = {}
    events = json.loads(path.read_text(encoding='utf-8'))
    if (title in events): return False
    events[title] = {
        "organiser": organiser,
        "phone": phone,
        "description": description
    }
    path.write_text(json.dumps(events,indent=4),encoding='utf-8')
    return True

def json_to_list():
    try:
        events = json.loads(path.read_text(encoding='utf-8'))
    except (FileNotFoundError, json.JSONDecodeError):
        events = {}
    return events

@route('/events')
@post('/events',method='post')
def load_events():
    events = json_to_list()
    
    if request.method == 'POST':
        title = request.forms.get('title')
        organiser = request.forms.get('organiser')
        phone = request.forms.get('phone')
        description = request.forms.get('describe')

        if all([title, organiser, phone, description]):
                if(len(check_events(title, organiser, phone, description)) == 0):
                    update_json(title, organiser, ''.join(re.split(r'[- \(\)]+',phone)) , description)
                    events = json_to_list()
                else:
                    return f"""
                    <script>
                        alert("{check_events(title, organiser, phone, description)}");
                        window.history.back();
                    </script>
                    """

    return template('events', events=events,title="Events",year=datetime.now().year)

def check_events(title, organizer, phone, description):
    try:
        error_message = ""

        if title == NULL:
            error_message += "Enter title "

        if len(title) > 50 or len(organizer) > 50:
            error_message += "Name is too long (>50 symbols) "

        if organizer == NULL:
            error_message += "Enter organizers name "

        if (re.search('[а-яА-Я]', title)) or (re.search('[а-яА-Я]', organizer) or (re.search('[а-яА-Я]', description))) :
            error_message += "There are Russian symbols "
            
        if not validate_phone(phone):
            error_message += "Wrong phone number "
            
        if len(description) > 500:
            error_message += "Description is too long (>500 symbols) "

        return error_message
    except Exception as e:
        error_message += e
        return error_message

def validate_phone(phone):
    pattern = re.compile(r'^(\+7|8)[-\s]?(\d{3}|\(\d{3}\))[-\s]?\d{3}[-\s]?\d\d[-\s]?\d\d$')
    return re.fullmatch(pattern, phone) is not None


