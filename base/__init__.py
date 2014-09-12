from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)

# Load the configuration from the instance folder
app.config.from_pyfile('config.py')
# Load the file specified by the BASE_CONFIG_FILE environment variable
app.config.from_envvar('BASE_CONFIG_FILE')

db = SQLAlchemy(app)



@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()