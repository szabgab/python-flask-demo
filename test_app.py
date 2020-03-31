from app import app

def test_app():
    web = app.test_client()
    rv = web.get('/')
    assert rv.status == '200 OK'
    assert b'<h1>Welcome to the Flask Demo</h1>' in rv.data
    #print(rv.data)


    rv = web.post('/', data = { "text": "FooBar" } )
    assert rv.status == '200 OK'
    assert b'<h1>Welcome to the Flask Demo</h1>' in rv.data
    assert b'<b>FooBar</b>' in rv.data

