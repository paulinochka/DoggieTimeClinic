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
    filePath = Path('dictionary.json') # путь до json-файла
    data = json.loads(filePath.read_text(encoding='utf-8')) #загрузка и чтение созданного файла
    mail = request.forms.get('ADRESS') #получение данных из поля ввода
    name = request.forms.get('NAME') #получение данных из поля ввода
    question = request.forms.get('QUEST') #получение данных из поля ввода
    checkMail = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z]+\.[a-zA-Z]{2,}$' #паттерн для проверки корректного ввода почты
    time = datetime.datetime.now() #получение текущей даты
    timeString = time.strftime("%Y-%m-%d") #перевод времени в строку
    if re.fullmatch(r'\d+', question): #проверка на ввод только цифр
        return name + ", sorry, this question contains only numbers! Answer date: " + timeString
    if mail == "" or name == "" or question == "": #проверка на пустые поля
        return "Field(s) is empty. Try again"
    mailData = mail
    questionData = question
    nameData = name
    check = False
    try: #проверка на корректный ввод почты
        if validate_email(mailData):
            check = True         
    except EmailNotValidError as exception:
        return name + ", sorry, this mail is incorrect. Try again. Answer date: " + timeString 

    if check:
        if (mailData in data): #поиск совпадающих почтовых адресов
            for quest in data[mailData]:
                if quest[0] == questionData: #проверка на уже сохранённый вопрос
                    return name + ", sorry, this question was already asked before. Answer date: " + timeString[mailData].append([questionData, nameData])
                else: 
                    data[mailData] = [[questionData, nameData]] #если такого вопроса не существует, то запись в файл
                    filePath.write_text(json.dumps(data, indent=4), encoding='utf-8') #запись полученных данных в json-файл
                    return name + ", great! The answer will be sent to the mail. " + mail + " Answer date: " + timeString  
    else:
        return name + ", sorry, this mail is incorrect. Try again. Answer date: " + timeString 
    
    
    
