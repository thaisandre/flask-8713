from flask_restplus import Api
from flask import Blueprint

api_bp = Blueprint('api', __name__, url_prefix='/api')

api = Api(version='1.0', title='Contas API',
      description='Api de Contas do curso PY-14')
api.init_app(api_bp)


from my_api.resources.conta_resource import ns as conta_resource
api.add_namespace(conta_resource, path='/contas')