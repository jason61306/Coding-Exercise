from flask import Blueprint, Response, json
import sqlite3

tasks = Blueprint(name="tasks", import_name=__name__)

@tasks.route('/', methods=['GET'])
def listTasks():    
  """
    get:
      description: list all tasks      
    responses:   
      '200':               
        content:
          application/json
          sample:
            {"result": [{"id": 1, "name": "name", "status": 0}]}
  """

  conn = sqlite3.connect("db")
  _c = conn.cursor()   
  _c.execute("SELECT * from tasks")

  tasks = _c.fetchall()
  conn.close()

  output = {}
  task_arr = []
  for task in tasks:
    task_obj = {}
    task_obj['id'] = task[0]
    task_obj['name'] = task[1]
    task_obj['status'] = task[2]
    task_arr.append(task_obj)

  output['result'] = task_arr        
  
  return Response (response=json.dumps(output), status=200, mimetype='application/json')

