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


def createRealm():
    payload = {}
    req = requests.post("http://localhost:8080/auth/admin/realms/master/", data=json.dumps(
        payload), headers={"content-type": 'application/json', "Authorization": "Bearer " + getToken()})
    print('Response: ' + str(req.status_code))
    return(req.status_code)

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
    print('\nResponse: ' + str(req.status_code))
    return(req.status_code)


def createGroups():
    payload = {}
    req = requests.post("http://localhost:8080/auth/admin/realms/master/", data=json.dumps(
        payload), headers={"content-type": 'application/json', "Authorization": "Bearer " + getToken()})
    print('Response: ' + str(req.status_code))
    return(req.status_code)


def createRoles():
    payload = {}
    req = requests.post("http://localhost:8080/auth/admin/realms/master/", data=json.dumps(
        payload), headers={"content-type": 'application/json', "Authorization": "Bearer " + getToken()})
    print('Response: ' + str(req.status_code))

#run the functions and return whether they were success for not. 
def loadinIf():
    if createRealm() == '201':
        print('Success \n')
    else:
        print('Failed: 500\n')
    if createUsers() == 201:
        print('Success \n')
    else:
        print('Failed: 500\n')
    if createGroups() == '201':
        print('Success \n')
    else:
        print('Failed: 500\n')
    if createRoles() == '201':
        print('Success \n')
    else:
        print('Failed: 500\n')





if __name__ == "__main__":
    loadinIf()
else:
    raise ValueError('you broke it you fool')
