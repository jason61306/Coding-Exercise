from flask import Flask

# load modules
from src.api.tasks import tasks
from src.api.task import task

# init Flask app
app = Flask(__name__)
# register blueprints
app.register_blueprint(tasks, url_prefix="/tasks")
app.register_blueprint(task, url_prefix="/task")
app.url_map.strict_slashes = False

if __name__ == "__main__":    
    app.run(host='0.0.0.0', debug=True)
