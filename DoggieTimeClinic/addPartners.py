from datetime import datetime
from bottle import route, template, post, request
import json
import re
from pathlib import Path

path = Path('static/otherFiles/partners.json') 
def update_json(name,phone,description):
    try:
        partners = json.loads(path.read_text(encoding='utf-8'))
    except (FileNotFoundError, json.JSONDecodeError):
        partners = {}
    partners = json.loads(path.read_text(encoding='utf-8'))
    if (name in partners): return False
    partners[name] = {
        "phone": phone,
        "description": description
    }
    path.write_text(json.dumps(partners,indent=4),encoding='utf-8')
    return True

def json_to_list():
    try:
        partners = json.loads(path.read_text(encoding='utf-8'))
    except (FileNotFoundError, json.JSONDecodeError):
        partners = {}
    return partners

@route('/partners')
@post('/partners',method='post')
def load_partners():
    partners = json_to_list()
    
    if request.method == 'POST':
        name = request.forms.get('name')
        phone = request.forms.get('phone')
        description = request.forms.get('describe')

        if all([name, phone, description]):
            update_json(name, phone, description)
            partners = json_to_list()

    return template('partners', partners=partners,title="Partners",year=datetime.now().year)
