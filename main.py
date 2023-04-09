from bottle import Bottle, route, run, template

app = Bottle()

@app.get('/')
def home():
    return '<h1>Hello World!</h1>'

@app.get('/hello/<name>')
def index(name):
    return template('<h2>Hello {{name}}!</h2>', name=name)

if __name__ == '__main__':
    run(app, host='0.0.0.0', port=3000)
