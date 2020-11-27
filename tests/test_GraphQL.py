import requests

headers = {
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Origin': 'http://localhost:5000',
}

data = '{"query":"query {\\n hello {\\n word\\n }\\n}"}'

response = requests.post('http://localhost:5000/graphql', headers=headers, data=data)

def test_GraphQL():
    assert b'{"data":{"hello":{"word":"sup dawg"}}}\n' == response.content