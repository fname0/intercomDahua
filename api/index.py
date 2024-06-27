from flask import Flask
import requests
from requests.auth import HTTPDigestAuth

app = Flask(__name__)

@app.route('/')
def home():
    params = {
        'action': 'openDoor',
        'channel': '1',
        'UserID': '101',
        'Type': 'Remote',
    }

    response = requests.get(
        'http://10.35.128.164/cgi-bin/accessControl.cgi',
        params=params,
        auth=HTTPDigestAuth('admin', 'PG19mega'),
    )
    return response.content
