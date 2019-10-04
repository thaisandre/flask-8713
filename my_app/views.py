from flask import Blueprint, render_template, request, redirect, url_for
from my_app.models import Conta
from my_app.db import get_connection

conta_bp = Blueprint('contas', __name__, url_prefix='/contas')

@conta_bp.route('/form')
def formulario():
    return render_template('form.html')

@conta_bp.route('/cria_conta', methods=['POST'])
def salva():
    numero = request.form.get('numero')
    titular = request.form.get('titular')
    saldo = float(request.form.get('saldo'))
    limite = float(request.form.get('limite'))

    conta = Conta(numero, titular, saldo, limite)

    conn = get_connection()

    sql = 'insert into contas (numero, titular, saldo, limite) values (%s, %s, %s, %s)'
    valores = (conta.numero, conta.titular, conta.saldo, conta.limite)

    cursor = conn.cursor()
    cursor.execute(sql, valores)

    conn.commit()
    conn.close()

    return redirect(url_for('contas.lista'))


@conta_bp.route('/lista', methods=['GET'])
def lista():
    # pegar os dados do banco
    conn = get_connection()

    sql = 'select * from contas'
    cursor = conn.cursor()
    cursor.execute(sql)

    resultado = cursor.fetchall()
    contas = []
    print(resultado)
    for registro in resultado:
        conta = Conta(registro[1], registro[2], registro[3], registro[4], registro[0])
        contas.append(conta)

    conn.close()

    # disponibilizar para a lista.html
    return render_template('lista.html', contas=contas)













