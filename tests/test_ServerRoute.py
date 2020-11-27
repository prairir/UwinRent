import urllib.request

response = urllib.request.urlopen('http://localhost:5000')
code = response.read()

def test_ServerRoute():
    assert b'something' == code