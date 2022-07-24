from flask import Flask
import sqlite3

# load modules
from src.api.tasks import tasks
from src.api.task import task

# init Flask app
app = Flask(__name__)
# register blueprints
app.register_blueprint(tasks, url_prefix="/tasks")
app.register_blueprint(task, url_prefix="/task")
app.url_map.strict_slashes = False

def init_db():
    conn = sqlite3.connect("db")
    _c = conn.cursor() 
    _c.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name TEXT NOT NULL, status BOOLEAN NOT NULL CHECK (status IN (0, 1)))")      
    conn.commit()
    conn.close()

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')

if __name__ == "__main__":    
    app.run(host='0.0.0.0', debug=True)
