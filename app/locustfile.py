import json
from locust import HttpUser,task,between

"""samples = [
    {"url":"https://images.unsplash.com/photo-1655709225251-5fcd01831217?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8MTl8fHxlbnwwfHx8fA%3D%3D&auto=format&fit=crop&w=600&q=60",
    "request_id":"12098"},
    {"url":"https://media.istockphoto.com/photos/shot-of-a-female-mechanic-talking-on-her-cellphone-while-working-in-picture-id1342082733?b=1&k=20&m=1342082733&s=170667a&w=0&h=lmEivEw1PblHsjRtOIka30dCe-OToNmo_AWmofY6m8M=",
    "request_id": "4423512342"},
    {"url": "https://images.unsplash.com/photo-1654922207552-4bdc8b4808e4?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8MTR8fHxlbnwwfHx8fA%3D%3D&auto=format&fit=crop&w=600&q=60",
    "request_id": "94874774387"}
]"""

class PerformanceTest(HttpUser):
    wait_time = between(4,6)

    @task()
    def test_fast_api(self):
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'X-Caller-ID':'avatar'}
        self.client.post("/api", json = {
            "url": "https://images.unsplash.com/photo-1654922207552-4bdc8b4808e4?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8MTR8fHxlbnwwfHx8fA%3D%3D&auto=format&fit=crop&w=600&q=60",
            "request_id": "94874774387"}, 
            headers = headers)



