import datetime
from pathlib import Path
import re
import pdb
import json
from bottle import post, request
from email_validator import validate_email, EmailNotValidError

@post('/events', method='post')
def my_form():
    dictionary = {}
    # mail = request.forms.get('ADRESS')
    # return "Thanks! The answer will be sent to the mail %s" % mail
    filePath = Path('dictionary.json') # ���� �� json-�����
    data = json.loads(filePath.read_text(encoding='utf-8')) #�������� � ������ ���������� �����
    mail = request.forms.get('ADRESS') #��������� ������ �� ���� �����
    name = request.forms.get('NAME') #��������� ������ �� ���� �����
    question = request.forms.get('QUEST') #��������� ������ �� ���� �����
    checkMail = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z]+\.[a-zA-Z]{2,}$' #������� ��� �������� ����������� ����� �����
    time = datetime.datetime.now() #��������� ������� ����
    timeString = time.strftime("%Y-%m-%d") #������� ������� � ������
    if re.fullmatch(r'\d+', question): #�������� �� ���� ������ ����
        return name + ", sorry, this question contains only numbers! Answer date: " + timeString
    if mail == "" or name == "" or question == "": #�������� �� ������ ����
        return "Field(s) is empty. Try again"
    mailData = mail
    questionData = question
    nameData = name
    check = False
    try: #�������� �� ���������� ���� �����
        if validate_email(mailData):
            check = True         
    except EmailNotValidError as exception:
        return name + ", sorry, this mail is incorrect. Try again. Answer date: " + timeString 

    if check:
        if (mailData in data): #����� ����������� �������� �������
            for quest in data[mailData]:
                if quest[0] == questionData: #�������� �� ��� ���������� ������
                    return name + ", sorry, this question was already asked before. Answer date: " + timeString[mailData].append([questionData, nameData])
                else: 
                    data[mailData] = [[questionData, nameData]] #���� ������ ������� �� ����������, �� ������ � ����
                    filePath.write_text(json.dumps(data, indent=4), encoding='utf-8') #������ ���������� ������ � json-����
                    return name + ", great! The answer will be sent to the mail. " + mail + " Answer date: " + timeString  
    else:
        return name + ", sorry, this mail is incorrect. Try again. Answer date: " + timeString 
    
    
    
