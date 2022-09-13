import requests
import json
import time
from datetime import datetime
import random

HOST = "localhost"  # Standard loopback interface address (localhost)
PORT = 8000  # Port to listen on (non-privileged ports are > 1023)
data_pattern = "{},{},{}\n"
sensorid = [1, 2]

if __name__ == '__main__':
    data = {}
    data['sensorid'] = random.choice(sensorid)
    data['timestamp'] = int(datetime.timestamp(datetime.now()))
    data['value'] = random.randint(10, 60)
    print(data)
    response = requests.post('http://{}:{}/api/data'.format(HOST, PORT), data=data)
    print(response)