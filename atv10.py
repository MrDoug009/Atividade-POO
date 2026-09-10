from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/cursos')
def obter_cursos():
    instituicao = request.args.get('instituicao')
    if instituicao == 'ifpr':
        cursos_ifpr = [
            {"id": 4, "nome": "Informática", "instituicao": "IFPR", "duracao": "4 anos"},
            {"id": 5, "nome": "Agroecologia", "instituicao": "IFPR", "duracao": "3 anos"},
            {"id": 6, "nome": "Administração", "instituicao": "IFPR", "duracao": "4 anos"}
        ]
        return jsonify(cursos_ifpr)

    cursos = [
        {"id": 1, "nome": "Engenharia de Software", "instituicao": "UTFPR", "duracao": "5 anos"},
        {"id": 2, "nome": "Medicina", "instituicao": "UFPR", "duracao": "6 anos"},
        {"id": 3, "nome": "Direito", "instituicao": "UEL", "duracao": "5 anos"}
    ]
    return jsonify(cursos)

@app.route('/cursos/<int:id>')
def obter_curso_por_id(id):
    curso = {"id": id, "nome": "Análise e Desenvolvimento de Sistemas", "instituicao": "IFPR", "duracao": "3 anos"}
    return jsonify(curso)

app.run(debug=True)