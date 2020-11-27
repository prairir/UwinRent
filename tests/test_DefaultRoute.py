import urllib.request

response = urllib.request.urlopen('http://localhost:5000')
code = response.getcode()

def test_ServerRoute():
    assert 200 == code