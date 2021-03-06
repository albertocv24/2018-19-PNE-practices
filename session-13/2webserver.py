import http.server
import socketserver

# Define the Server's port
PORT = 8009




class TestHandler(http.server.BaseHTTPRequestHandler):





    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # We just print a message
        print("GET received!")

        print('Request line:' + self.requestline)
        print('Command: ' + self.command)
        print('Path: ' + self.path)

        content = ''

        if self.path == '/':
            file='index.html'
        else:
            file='error.html'

        with open(file, 'r') as f:
            for line in f:
                content += line

        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Length-Type', len(str.encode(content)))
        self.end_headers()

        self.wfile.write(str.encode(content))

        # IN this simple server version:
        # We are NOT processing the client's request
        # We are NOT generating any response message
        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()

print("")
print("Server Stopped")