from http.client import HTTPConnection
from urllib.parse import urlencode
import json

def query_objects(host, url, namelist):
    conn = HTTPConnection(host)
    headers = {
        'Content-Type': 'text/json',
    }

    data = {'names':namelist}

    conn = HTTPConnection(host)
    conn.request('POST', url, body=json.dumps(data), headers=headers)
    resp = conn.getresponse()
    print(resp.status, resp.reason)

    data = resp.read()
    print(data.decode('utf-8'))
    objlist= json.loads(data)
    print(objlist)

    conn.close()
    return objlist


if __name__ == '__main__':
    namelist = ['r','g','b']
    query_objects('127.0.0.1:8000', '/', namelist)