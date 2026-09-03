from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/alunos')
def obter_alunos():
    nome = request.args.get('nome')
    if nome:
        aluno = {"id": 1, "nome": "João", "curso": "Informatica", "idade": 18}
        return jsonify(aluno)

    alunos = [
        {"id": 1, "nome": "João", "curso": "Informatica", "idade": 18},
        {"id": 2, "nome": "Maria", "curso": "Enfermagem", "idade": 20},
        {"id": 3, "nome": "Pedro", "curso": "Administracao", "idade": 22}
    ]
    return jsonify(alunos)

@app.route('/alunos/<int:id>')
def obter_aluno_por_id(id):
    aluno = {"id": id, "nome": "Lucas", "curso": "Agropecuaria", "idade": 19}
    return jsonify(aluno)

app.run(debug=True)