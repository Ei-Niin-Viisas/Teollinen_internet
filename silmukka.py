import os, requests
from requests.auth import HTTPDigestAuth
from datetime import datetime
from time import sleep

url_iosystem_gripper = 'http://127.0.0.1:8081/rw/iosystem/signals/DI_Gripper1_Closed'
url_iosystem_tcpspeed = 'http://127.0.0.1:8081/rw/iosystem/signals/AO_TCP_SPEED'
username = 'Default User'
password = 'robotics'
#url = 'http://roboticsflaskserver.azurewebsites.net/api/robotics'
url = "http://localhost:5000/api/robotics"

while True: 
    params = {'json': '1'}
    response = requests.get(
        url_iosystem_tcpspeed,
        auth=HTTPDigestAuth(username, password),
        params=params
    )
    data = response.json()
    speed = data['_embedded']['_state'][0]['lvalue']
    time = datetime.now()
    requests.post(url, data = {"tcp_speed": speed, "time": time, "gripper_state" : 0})
    print({"tcp_speed": speed, "time": time})
    sleep(5)
    