from datetime import datetime
from bottle import route, template, post, request
import json
import re
from pathlib import Path

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
            update_json(title, organiser, phone, description)
            events = json_to_list()  # Обновляем события после добавления

    return template('events', events=events,title="Events",year=datetime.now().year)


