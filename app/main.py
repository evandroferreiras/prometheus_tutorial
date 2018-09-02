from prometheus_client import start_http_server, Summary, Counter, Histogram
import random
import time


REQUEST_TIME_HIST = Histogram('request_latency_seconds', 'Histogram')


COUNTER = Counter('requests_greater_than_half_sec_total',
                  'number of waits greater than half a second')


@REQUEST_TIME_HIST.time()
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
