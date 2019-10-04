from flask_restplus import fields
from my_api import api

conta_output_dto = api.model('conta', {
    "id": fields.Integer,
    "numero": fields.String,
    "titular": fields.String,
    "saldo": fields.Float,
    "limite": fields.Float,
})

conta_input_dto = api.model('conta', {
    "numero": fields.String,
    "titular": fields.String,
    "saldo": fields.Float,
    "limite": fields.Float
})