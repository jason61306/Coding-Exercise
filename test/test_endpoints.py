import os
import requests

def test_listTasks(api):
    endpoint = os.path.join(api, 'tasks')
    response = requests.get(endpoint)
    assert response.status_code == 200
    json = response.json()
    assert 'result' in json    

def test_createTask(api):
    endpoint = os.path.join(api, 'task')
    payload = {'name': 'test'}
    response = requests.post(endpoint, json=payload)
    assert response.status_code == 201
    json = response.json()
    assert 'result' in json
    assert json['result']['name'] == "test"

def test_updateTask(api):
    endpoint = os.path.join(api, 'task', '1')
    payload = {'name': 'test','status': 1,'id': 1}
    response = requests.put(endpoint, json=payload)
    assert response.status_code == 200
    json = response.json()
    assert 'result' in json
    assert json['result']['name'] == "test"
    assert json['result']['status'] == 1

def test_deleteTask(api):
    endpoint = os.path.join(api, 'task', '1')    
    response = requests.delete(endpoint)
    assert response.status_code == 200