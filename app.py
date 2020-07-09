#Setup Script inital and support config changes
#Open to discussion and renewal
import json
import sys

import requests


def readConfig(self):
    return None

def getToken():
    docdict = {
        'grant_type': "password",
        'username': "admin",
        'password': "admin",
        'client_id': "admin-cli"
    }
    getTokenQuery = requests.post('http://localhost:8080/auth/realms/master/protocol/openid-connect/token', data=docdict)
    token = getTokenQuery.json()['access_token']
    return token

def createUsers():
    payload = {
        "email": "jimbob@gmail.com",
        "username": "jimbob@gmail.com",
        "enabled": True,
        "firstName": "service",
        "lastName": "account",
        "credentials": [{"value": "secret", "type": "password", }],
    }

    req = requests.post("http://localhost:8080/auth/admin/realms/master/users", data=json.dumps(payload), headers=    {"content-type": 'application/json', "Authorization": "Bearer " + getToken()})
    
    print('Response: ' + str(req.status_code))

def createGroups():
    payload = {}
    req = requests.post("http://localhost:8080/auth/admin/realms/master/", data=json.dumps(
        payload), headers={"content-type": 'application/json', "Authorization": "Bearer " + getToken()})




if __name__ == "__main__":
    createUsers()
else:
    raise ValueError('you broke it you fool')
