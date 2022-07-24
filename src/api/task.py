from flask import Blueprint, request, Response, json
import sqlite3

task = Blueprint(name="task", import_name=__name__)

@task.route('/', methods=['POST'])
def createTask():    
  """
    post:
      description: create a new task
    requestBody:
        required: true
        content:
            application/json: 
            sample:
              {"name": "買晚餐"}                  
    responses:   
      '201':               
        content:
          application/json
          sample:
            {"result": [{"id": 1, "name": "買晚餐", "status": 0}]}
  """
  data = request.get_json()
  name = data['name']

  conn = sqlite3.connect("db")
  _c = conn.cursor()   
  _c.execute("INSERT INTO tasks(name, status) values(?, ?)", (name, False))
  conn.commit()
  _c.execute("SELECT * FROM tasks WHERE id = last_insert_rowid();")
  task = _c.fetchone()
  conn.close()

  output = {"result": {"id": task[0], "name": task[1], "status": task[2]}}
  return Response (response=json.dumps(output), status=201, mimetype='application/json')


@task.route('/<int:id>', methods=['PUT'])
def updateTask(id):    
  """
    put:
      description: update the task
    requestBody:
        required: true
        content:
            application/json: 
            sample:
              {"name": "買早餐","status": 1,"id": 1}         
    responses:   
      '200':               
        content:
          application/json
          sample:
            {"result": [{"id": 1, "name": "買晚餐", "status": 1}]}
  """
  data = request.get_json()
  name = data['name']
  status = data['status']

  conn = sqlite3.connect("db")
  _c = conn.cursor()   
  _c.execute("UPDATE tasks SET name=?, status=? WHERE id=?;", (name, status, id))
  conn.commit()
  conn.close()

  output = {"result": {"id": id, "name": name, "status": status}}
  return Response (response=json.dumps(output), status=200, mimetype='application/json')


@task.route('/<int:id>', methods=['DELETE'])
def deleteTask(id):    
  """
    delete:
      description: delete the task           
    responses:   
      '200'                       
  """

  conn = sqlite3.connect("db")
  _c = conn.cursor()
  _c.execute("DELETE FROM tasks WHERE id=?;", (id,))
  conn.commit()
  conn.close()
  return Response(status=200, mimetype='application/json')