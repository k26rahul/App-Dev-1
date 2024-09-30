from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    if self.path == '/':
      self.send_response(200)
      self.send_header("Content-type", "text/html")
      self.end_headers()
      response = f"hello Vidu :) from localhost at {self.server.server_port};"
      self.wfile.write(response.encode())

    else:
      self.send_response(404)
      self.end_headers()


PORT = 80

server_address = ('', PORT)
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
print(f"Starting http server on port {PORT}...")
httpd.serve_forever()
