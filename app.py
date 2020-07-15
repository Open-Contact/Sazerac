#Setup Script inital and support config changes
#Open to discussion and renewal
import json
import sys
import time
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


#Create opencontactdev realm RS512 email-verify false reg-allow false
def createRealm():
    payload = {}
    req = requests.post("http://localhost:8080/auth/admin/realms/master/", data=json.dumps(
        payload), headers={"content-type": 'application/json', "Authorization": "Bearer " + getToken()})
    print('\nResponse: ' + str(req.status_code))
    return(req.status_code)


#testagent
#testmanager
#testadmin
def createUsers():
    payload = {
        "email": "",
        "username": "admin",
        "enabled": True,
        "firstName": "",
        "lastName": "",
        "credentials": [{"value": "admin", "type": "password", }],
    }

    req = requests.post("http://localhost:8080/auth/admin/realms/opencontactdev/users", data=json.dumps(payload), headers=    {"content-type": 'application/json', "Authorization": "Bearer " + getToken()})
    print('Response: ' + str(req.status_code))
    return(req.status_code)

def getUsername():
    payload = {
        'search': 'admin'
    }
    req = requests.get("http://localhost:8080/auth/admin/realms/opencontactdev/users",
                       data=payload, headers={"Authorization": "Bearer " + getToken()})
    load = json.loads(req.text)
    for i in load:
        print(i['id'])

#agents - roles
#managers
#admins
def createGroups():
    payload = {}
    req = requests.post("http://localhost:8080/auth/admin/realms/master/", data=json.dumps(
        payload), headers={"content-type": 'application/json', "Authorization": "Bearer " + getToken()})
    print('Response: ' + str(req.status_code))
    return(req.status_code)


#agent
#manager
#admin
def createRoles():
    payload = {}
    req = requests.post("http://localhost:8080/auth/admin/realms/master/", data=json.dumps(
        payload), headers={"content-type": 'application/json', "Authorization": "Bearer " + getToken()})
    print('Response: ' + str(req.status_code))


#Agents agent
#Agents manager
#Agents admin
def addRoles():
    payload = {}
    req = requests.post("http://localhost:8080/auth/admin/realms/master/", data=json.dumps(
        payload), headers={"content-type": 'application/json', "Authorization": "Bearer " + getToken()})
    print('Response: ' + str(req.status_code))


#run the functions and return whether they were success for not. 
def loadinIf():
    # if createRealm() == 201:
    #     print('\nSuccess \n')
    # else:
    #     print('Failed: 500\n')
    if createUsers() == 201:
        print('Success \n')
    else:
        print('Failed: 500\n')
    # if createGroups() == 201:
    #     print('Success \n')
    # else:
    #     print('Failed: 500\n')
    # if createRoles() == 201:
    #     print('Success \n')
    # else:
    #     print('Failed: 500')
    time.sleep(1)
    print(
r"""
                                              __             __     
  ____  ____  ___  ____     _________  ____  / /_____ ______/ /_    
 / __ \/ __ \/ _ \/ __ \   / ___/ __ \/ __ \/ __/ __ `/ ___/ __/    
/ /_/ / /_/ /  __/ / / /  / /__/ /_/ / / / / /_/ /_/ / /__/ /_      
\____/ .___/\___/_/ /_/   \___/\____/_/ /_/\__/\__,_/\___/\__/      
    /_/                                                                 
"""
    )



if __name__ == "__main__":
    getUsername()
else:
    raise ValueError('you broke it you fool')
