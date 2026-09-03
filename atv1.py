from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/filmes')
def obter_filmes():
    filmes = [
        {"id": 1, "nome": "Matrix", "diretor": "Lana Wachowski", "ano": 1999},
        {"id": 10, "nome": "Inception", "diretor": "Christopher Nolan", "ano": 2010}
    ]

    return jsonify(filmes)

@app.route('/filmes/<int:id>')
def obter_filme_por_id(id):
    filme = {"id": id, "nome": "Inception", "diretor": "Christopher Nolan", "ano": 2010}
        
    
    
            
    return jsonify(filme)

app.run(debug=True)