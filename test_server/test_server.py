from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
import urllib
import test_object_generator
import json


class RandomPositionHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/json')
        self.end_headers()
        parsed = urllib.parse.parse_qs(self.path)
        j = json.dumps(parsed).encode('utf-8')
        #get_obj_list_with_xy_position(nameList, min, max)
        self.wfile.write(j)
        
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()

        received = json.loads(body)
        objlist = test_object_generator.get_obj_list_with_xy_position(received["names"], 1, 100)
        print(objlist)

        response = BytesIO()
        senddata = json.dumps(objlist).encode('utf-8')
        response.write(senddata)
        self.wfile.write(response.getvalue())

if __name__ == '__main__':
    port = 8000
    server = HTTPServer(('', port), RandomPositionHandler)
    print("Started WebServer on port", port, "...")
    print("Press ^C to quit WebServer.")
    server.serve_forever()