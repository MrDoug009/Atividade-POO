from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/cidades')
def obter_cidades():
    estado = request.args.get('estado')
    if estado == 'parana':
        cidades_pr = [
            {"id": 4, "nome": "Curitiba", "estado": "Paraná", "populacao": 1963726},
            {"id": 5, "nome": "Cascavel", "estado": "Paraná", "populacao": 348051},
            {"id": 6, "nome": "Quedas do Iguaçu", "estado": "Paraná", "populacao": 34749}
        ]
        return jsonify(cidades_pr)

    cidades = [
        {"id": 1, "nome": "São Paulo", "estado": "São Paulo", "populacao": 12325232},
        {"id": 2, "nome": "Rio de Janeiro", "estado": "Rio de Janeiro", "populacao": 6747815},
        {"id": 3, "nome": "Florianópolis", "estado": "Santa Catarina", "populacao": 516524}
    ]
    return jsonify(cidades)

@app.route('/cidades/<int:id>')
def obter_cidade_por_id(id):
    cidade = {"id": id, "nome": "Londrina", "estado": "Paraná", "populacao": 580870}
    return jsonify(cidade)

app.run(debug=True)