from bottle import Bottle, post, run, request, template, static_file
import json
import re
from pathlib import Path

path = Path('static/otherFiles/events.json') 
events = {}
def update_json(title,organiser,phone,description):
    events = json.loads(path.read_text(encoding='utf-8'))
    if (title in events): return False
    events[title] = []
    events[title].append([organiser, phone,description])
    path.write_text(json.dumps(events,indent=4),encoding='utf-8')
    return True

# Хранение событий (временное, для примера)
file = 'events.json'

@post('/events', method='post')
def load_events():
    title = request.forms.get('title');
    organiser = request.forms.get('organiser');
    phone = request.forms.get('phone');
    description = request.forms.get('describe');
    update_json(title,organiser,phone,description)
    return template('events_list', events=events)