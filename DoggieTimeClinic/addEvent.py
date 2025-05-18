from bottle import Bottle, post, run, request, template, static_file

app = Bottle()

# Хранение событий (временное, для примера)
events = []

@post('/events', method='post')
def add_event():
    event = {
        'title': request.forms.get('title'),
        'description': request.forms.get('description'),
        'date': request.forms.get('date'),
        'phone': request.forms.get('phone')
    }
    events.append(event)
    for event in events:
        print(event.title)
    return template('event_list', events=events)

# @post('/static/<filename:path>')
# def serve_static(filename):
#     return static_file(filename, root='./static')
