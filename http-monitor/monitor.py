import requests
from wsgiref.simple_server import make_server
from prometheus_client import make_wsgi_app, Gauge


url503 = "https://httpstat.us/503"
url200 = "https://httpstat.us/200"

metrics_responsetime = Gauge('sample_external_url_response_ms', 'Sample URL response time in milliseconds', ['url'])
metrics_up = Gauge('sample_external_url_up', 'Sample URL provided is up or not', ['url'])

def collectMetrics():
    response503 = requests.get(url503)
    response200 = requests.get(url200)

    status503 = response503.status_code
    status200 = response200.status_code

    responsetime200 = response200.elapsed.total_seconds()*1000
    responsetime503 = response503.elapsed.total_seconds()*1000

    if status503 == 200:
        metrics_up.labels(url='https://httpstat.us/503').set(1)
    else:
        metrics_up.labels(url='https://httpstat.us/503').set(0)
    
    if status200 == 200:
        metrics_up.labels(url='https://httpstat.us/200').set(1)
    else:
        metrics_up.labels(url='https://httpstat.us/200').set(0)
    
    metrics_responsetime.labels(url='https://httpstat.us/503').set(responsetime503)
    metrics_responsetime.labels(url='https://httpstat.us/200').set(responsetime200)
    
metrics_app = make_wsgi_app()

def my_app(env, start_func):
    if env['PATH_INFO'] == '/metrics':
            collectMetrics()
            return metrics_app(env, start_func)

httpd = make_server('', 8080, my_app)
httpd.serve_forever()


