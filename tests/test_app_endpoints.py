from webtest import TestApp
import sys
sys.path.append('../')
import main

def test_home_endpoint():
    app = TestApp(main.app)
    print(app.get('/').text)
    assert app.get('/').status_int == 200
    assert app.get('/').text  == '<h1>Hello World!</h1>'


def test_hello_endpoint():
    app = TestApp(main.app)
    print(app.get('/hello/Alex').text)
    assert app.get('/hello/Alex').status_int == 200
    assert app.get('/hello/Alex').text  == '<h2>Hello Alex!</h2>'
