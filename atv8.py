from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/jogos')
def obter_jogos():
    genero = request.args.get('genero')
    if genero == 'rpg':
        jogo_rpg = [{"id": 4, "nome": "The Witcher 3", "genero": "RPG", "ano": 2015}]
        return jsonify(jogo_rpg)

    jogos = [
        {"id": 1, "nome": "FIFA 23", "genero": "Esportes", "ano": 2022},
        {"id": 2, "nome": "Call of Duty", "genero": "FPS", "ano": 2019},
        {"id": 3, "nome": "Super Mario Odyssey", "genero": "Plataforma", "ano": 2017}
    ]
    return jsonify(jogos)

@app.route('/jogos/<int:id>')
def obter_jogo_por_id(id):
    jogo = {"id": id, "nome": "Skyrim", "genero": "RPG", "ano": 2011}
    return jsonify(jogo)

app.run(debug=True)