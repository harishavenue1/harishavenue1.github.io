from http.server import SimpleHTTPRequestHandler, HTTPServer

class CustomHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        SimpleHTTPRequestHandler.end_headers(self)

# Define the server address
server_address = ('', 8000)

# Create the server object
httpd = HTTPServer(server_address, CustomHandler)

# Start the server
print('Server running at http://localhost:8000/')
httpd.serve_forever()
