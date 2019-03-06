import time
from prometheus_client import Gauge

TIME = Gauge('time_seconds', 'The current time.')
TIME.set_function(lambda: time.time())
