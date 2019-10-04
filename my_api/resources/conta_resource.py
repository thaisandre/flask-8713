from flask_restplus import Resource, Namespace, marshal_with
from flask import request
from my_api.models.conta import Conta
from my_api.utils.serializers import conta_output_dto, conta_input_dto

ns =  Namespace('contas', description='operações das contas')

conta1 = Conta('123-4', 'João', 1200.0, 1000.0, 1)
conta2 = Conta('123-5', 'José', 1500.0, 1000.0, 2)
conta3 = Conta('123-6', 'Maria', 2200.0, 1000.0, 3)

contas  = [conta1, conta2, conta3]


@ns.route('/<int:i>')
class ContasResource(Resource):

    @marshal_with(conta_output_dto)
    def get(self):
        return Conta.query.all()

    def post(self):
        data = request.get_json()
        numero = data.get('numero')
        titular = data.get('titular')
        saldo = float(data.get('saldo'))
        limite = float(data.get('limite'))

        conta = Conta(numero, titular, saldo, limite)

        # adicionar no banco