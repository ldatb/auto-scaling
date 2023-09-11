"""
This contains sample code on load test scripts to load test REST API based services with locust.

To execute this file, first start a pipenv by issuing `pipenv shell`,
and then download all dependencies with `pipenv sync`. After that you
can run it in headless mode with: `locust -f locust.py --headless --users 50 --spawn-rate 2 -H http://localhost:5000`
"""

__author__ = "Lucas de Ataides"

from locust import HttpUser, task

class APITest(HttpUser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_start(self):
        pass

    @task
    def index(self):
        self.client.get("/")

    @task
    def square_root(self):
        self.client.get("/square-root")

    @task
    def cube_root(self):
        self.client.get("/cube-root")
