from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/musicas')
def obter_musicas():
    artista = request.args.get('artista')
    if artista == 'legiao':
        musicas_legiao = [
            {"id": 3, "nome": "Tempo Perdido", "artista": "Legião Urbana", "ano": 1986},
            {"id": 4, "nome": "Faroeste Caboclo", "artista": "Legião Urbana", "ano": 1987}
        ]
        return jsonify(musicas_legiao)

    musicas = [
        {"id": 1, "nome": "Bohemian Rhapsody", "artista": "Queen", "ano": 1975},
        {"id": 2, "nome": "Hotel California", "artista": "Eagles", "ano": 1976}
    ]
    return jsonify(musicas)

@app.route('/musicas/<int:id>')
def obter_musica_por_id(id):
    musica = {"id": id, "nome": "Pais e Filhos", "artista": "Legião Urbana", "ano": 1989}
    return jsonify(musica)

app.run(debug=True)