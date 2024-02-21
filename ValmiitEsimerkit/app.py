import requests
from flask import Flask
from requests.auth import HTTPDigestAuth
from datetime import datetime


app = Flask(__name__)

url_iosystem_gripper = 'http://127.0.0.1:8081/rw/iosystem/signals/DI_Gripper1_Closed'
url_iosystem_tcpspeed = 'http://127.0.0.1:8081/rw/iosystem/signals/AO_TCP_SPEED'
username = 'Default User'
password = 'robotics'

@app.route('/get_gripper_state', methods=['GET'])
def get_gripper_state():
    params = {'json': '1'}
    response = requests.get(
        url_iosystem_gripper,
        auth=HTTPDigestAuth(username, password),
        params=params
    )
    data = response.json()
    state = data['_embedded']['_state'][0]['lvalue']
    time = datetime.now()
    return {"gripper_state": state, "time": time}

@app.route('/get_tcp_speed')
def get_tcp_speed():
    params = {'json': '1'}
    response = requests.get(
        url_iosystem_tcpspeed,
        auth=HTTPDigestAuth(username, password),
        params=params
    )
    data = response.json()
    speed = data['_embedded']['_state'][0]['lvalue']
    time = datetime.now()
    return {"tcp_speed": speed, "time": time}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')