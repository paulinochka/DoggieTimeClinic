from bottle import Bottle, run, request, static_file, template, route, view
import re
import json
import os

app = Bottle()
QUESTIONS_FILE = "questions.json"

# Проверка данных
def is_valid_email(email):
    return re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email) is not None

def is_valid_phone(phone):
    return re.match(r'^(\+7|7|8)?[\s\-]?\(?\d{3}\)?[\s\-]?\d{3}[\s\-]?\d{2}[\s\-]?\d{2}$', phone) is not None

# Работа с JSON
def load_questions():
    if not os.path.exists(QUESTIONS_FILE):
        return []  
    
    with open(QUESTIONS_FILE, 'r') as f:
        try:
            data = json.load(f)
            if isinstance(data, list): 
                return data
            else:  
                return []
        except json.JSONDecodeError:  
            return []

def save_question(name, email, phone, question):
    data = load_questions()
    data.append({"name": name, "email": email, "phone": phone, "question": question})
    with open(QUESTIONS_FILE, 'w') as f:
        json.dump(data, f, indent=2)
@app.route('/static/<filename:path>')
def serve_static(filename):
    return static_file(filename, root='./static')

