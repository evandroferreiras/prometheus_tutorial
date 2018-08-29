from prometheus_client import start_http_server, Summary, Counter, Histogram
import random
import time

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds',
                       'Time spent processing request')

REQUEST_TIME_HIST = Histogram('request_latency_seconds', 'Histogram')


COUNTER = Counter('count_bigger_half_sec',
                  'number of waits greater than half a second')


@REQUEST_TIME_HIST.time()
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)


if __name__ == '__main__':
    start_http_server(5000)
    while True:
        rnd = random.random()
        if rnd > 0.5:
            COUNTER.inc()
        process_request(rnd)
