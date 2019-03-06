import http.server
from prometheus_client import start_http_server, Gauge
import time


# Track the number of calls in progress and when the last oen was completed
INPROGRESS = Gauge('hello_worlds_inprogress', 'Number of Hello Worlds in Progress.')
LAST = Gauge('hello_world_last_time_seconds', 'The last time a Hello World was served.')

class MyHandler(http.server.BaseHTTPRequestHandler):
    @INPROGRESS.track_inprogress()
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello World")
        LAST.set_to_current_time()

if __name__ == "__main__":
    start_http_server(8000)
    server = http.server.HTTPServer(('localhost', 8001), MyHandler)
    server.serve_forever()
