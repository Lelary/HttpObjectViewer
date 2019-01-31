from http.client import HTTPConnection
from urllib.parse import urlencode

def example_get(host, url):
    conn = HTTPConnection(host)
    conn.request('GET', url)
    response = conn.getresponse()
    data = response.read()
    conn.close()

    print(response.status, response.reason)
    print(data.decode())

def example_post(host, url):
    conn = HTTPConnection(host)
    params = urlencode({
        'language': 'python',
        'name': 'aaa',
    })
    headers = {
        'Accept': 'text/plain'
    }

    conn = HTTPConnection(host)
    conn.request('POST', url, params, headers)
    resp = conn.getresponse()
    print(resp.status, resp.reason)

    data = resp.read()
    print(data.decode('utf-8'))

    conn.close()


if __name__ == '__main__':
    example_get('www.google.com', '/')
    example_post('127.0.0.1:8000', '/')