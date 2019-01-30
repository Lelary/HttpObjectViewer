from http.client import HTTPConnection
from urllib.parse import urlencode
import json

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
    headers = {
        'Content-Type': 'text/json',
    }

    data = {'names':['aaa','bbb','ccc']}

    conn = HTTPConnection(host)
    conn.request('POST', url, body=json.dumps(data), headers=headers)
    resp = conn.getresponse()
    print(resp.status, resp.reason)

    data = resp.read()
    print(data.decode('utf-8'))
    objlist= json.loads(data)
    print(objlist)

    conn.close()


if __name__ == '__main__':
    example_post('127.0.0.1:8000', '/')