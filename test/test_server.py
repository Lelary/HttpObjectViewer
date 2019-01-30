from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Hello World")

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())

if __name__ == '__main__':
    port = 8000
    server = HTTPServer(('', port), MyHandler)
    print("Started WebServer on port", port, "...")
    print("Press ^C to quit WebServer.")
    server.serve_forever()