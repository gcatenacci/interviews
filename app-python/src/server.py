from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
from datetime import datetime
from threading import Thread
import requests

PORT_MESSAGES = {
    8080: "Hello from 8080",
    9090: "Hello from 9090"
}

def send_heartbeat(port):
    requests.get(f"http://localhost:9999/heartbeat?port={port}")  # Simulated heartbeat

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        port = self.server.server_port
        message = PORT_MESSAGES.get(port, "Unknown port")

        logging.info(f"{datetime.utcnow().isoformat()} - Accessed port {port}")
        send_heartbeat(port)

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode('utf-8'))

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    def start_server(port):
        server = HTTPServer(('0.0.0.0', port), SimpleHandler)
        logging.info(f"Starting server on port {port}")
        server.serve_forever()

    Thread(target=start_server, args=(8080,)).start()
    Thread(target=start_server, args=(9090,)).start()
