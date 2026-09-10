from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/funcionarios')
def obter_funcionarios():
    cargo = request.args.get('cargo')
    if cargo == 'programador':
        programadores = [
            {"id": 1, "nome": "Ana", "cargo": "Programador", "salario": 5000.0},
            {"id": 2, "nome": "Carlos", "cargo": "Programador", "salario": 5500.0}
        ]
        return jsonify(programadores)

    funcionarios = [
        {"id": 3, "nome": "Marcos", "cargo": "Gerente", "salario": 8000.0},
        {"id": 4, "nome": "Julia", "cargo": "Analista de RH", "salario": 4000.0},
        {"id": 5, "nome": "Fernanda", "cargo": "Designer", "salario": 4500.0}
    ]
    return jsonify(funcionarios)

@app.route('/funcionarios/<int:id>')
def obter_funcionario_por_id(id):
    funcionario = {"id": id, "nome": "Roberto", "cargo": "Diretor", "salario": 12000.0}
    return jsonify(funcionario)

app.run(debug=True)