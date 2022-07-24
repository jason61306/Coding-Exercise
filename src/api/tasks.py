from flask import Blueprint, Response

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
  
  return Response (response={}, status=200, mimetype='application/json')

