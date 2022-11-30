#!/usr/bin/env python3
import multiprocessing
import time

from gunicorn_server import StandaloneApplication
from falcon import App


app = App()


class Resource:

    def on_get(self, req, resp):
        time.sleep(0.2)
        resp.text = 'Ok'


app.add_route('/', Resource())


if __name__ == "__main__":
    gunicorn_app = StandaloneApplication(app, options={
        'bind': '127.0.0.1:8080',
        'workers': (multiprocessing.cpu_count() * 2) + 1,
        'worker_class': 'meinheld.gmeinheld.MeinheldWorker'
    })
    gunicorn_app.run()
