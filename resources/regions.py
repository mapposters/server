from flask.ext import restful

class RegionsResource(restful.Resource):
  path = "/regions"
  def get(self):
    return [
      {"name":"Toronto"},
      {"name":"Vancouver"},
      {"name":"Calgaru"},

    ]
