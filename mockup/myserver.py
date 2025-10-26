from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        # Risponde a tutte le richieste GET
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        response = {
            'message': 'Richiesta GET ricevuta',
            'path': self.path,
            'method': 'GET'
        }
        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        # Risponde a tutte le richieste POST
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        response = {
            'message': 'Richiesta POST ricevuta',
            'path': self.path,
            'method': 'POST',
            'data': post_data.decode()
        }
        self.wfile.write(json.dumps(response).encode())

    def log_message(self, format, *args):
        # Disabilita i log automatici
        return

def run_server():
    server_address = ('', 8080)  # Ascolta su tutte le interfacce
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print('Server in esecuzione sulla porta 8080...')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
