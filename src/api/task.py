from flask import Blueprint, Response

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
  return Response (response={}, status=201, mimetype='application/json')


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
  return Response (response={}, status=200, mimetype='application/json')


@task.route('/<int:id>', methods=['DELETE'])
def deleteTask(id):    
  """
    delete:
      description: delete the task           
    responses:   
      '200'                       
  """
  return Response(status=200, mimetype='application/json')