from asyncio.windows_events import NULL
from datetime import datetime
from bottle import route, template, post, request
import json
import re
from pathlib import Path

path = Path('static/otherFiles/partners.json') 
errors = {}
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
                if(len(check_partners(name, phone, description)) == 0):
                    update_json(name, ''.join(re.split(r'[- \(\)]+',phone)) , description)
                    partners = json_to_list()
                else:
                    return f"""
                    <script>
                        alert("{check_partners(name, phone, description)}");
                        window.history.back();
                    </script>
                    """
        return template('partners', partners=partners,title="Partners",year=datetime.now().year)

def check_partners(name, phone, description):
    try:
        error_message = ""
        if name == NULL:
            error_message += "Enter name "

        if len(name) > 50:
            error_message += "Name is too long (>50 symbols) "

        if (re.search('[а-яА-ЯёЁ]', name)):
            error_message += "There are Russian symbols "
            
        if not validate_phone(phone):
            error_message += "Wrong phone number "
            
        if len(description) > 500:
            error_message += "Description is too long (>500 symbols) "

        if (re.search('[а-яА-ЯёЁ]', description)):
            error_message += "There are Russian symbols "

        return error_message
    except Exception as e:
        error_message += e
        return error_message

def validate_phone(phone):
    pattern = re.compile(r'^(\+7|8)[-\s]?(\d{3}|\(\d{3}\))[-\s]?\d{3}[-\s]?\d\d[-\s]?\d\d$')
    return re.fullmatch(pattern, phone) is not None