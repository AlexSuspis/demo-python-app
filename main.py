from bottle import route, run, template

@route('/')
def home():
    return '<h1>Hello World!</h1>'

@route('/hello/<name>')
def index(name):
    return template('<h2>Hello {{name}}!</h2>', name=name)

run(host='localhost', port=8081)
