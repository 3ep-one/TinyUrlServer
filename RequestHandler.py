from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
import json
from UrlShortner import UrlShortener


class HttpHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(400)
        self.end_headers()
        self.wfile.write(b'Bad request method!')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        response = BytesIO()
        request_body_dict = json.loads(body.decode('utf8'))
        if('url' in request_body_dict):
            request_url = request_body_dict['url']
            url_shortener = UrlShortener()
            shortend_url = url_shortener.shorten_url(str(request_url))
            json_response = json.dumps({request_url: shortend_url})
            self.send_response(200)
            self.end_headers()
            response.write(json_response.encode('utf8'))
            self.wfile.write(response.getvalue())
        else:
            self.send_response(400)
            self.end_headers()
            response.write(b'Bad request param!')
            self.wfile.write(response.getvalue())


httpd = HTTPServer(('127.0.0.1', 8000), HttpHandler)
httpd.serve_forever()
