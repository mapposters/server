from flask import Flask
from flask.ext import restful
import resources
import os

import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
# handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

app.logger.info('Good Morning, Vietnam! app.py starts up')
if os.environ.get('WHERE_AM_I'):
  app.logger.info('Initializing DEV config..')
  app.config.from_pyfile('config/development.py')
else:
  app.logger.info('Initializing PROD config.. (set up environ $WHERE_AM_I for DEV)')
  app.config.from_pyfile('config/production.py')

api = restful.Api(app)
api.add_resource(resources.RegionsResource, resources.RegionsResource.path)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
