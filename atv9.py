from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/restaurantes')
def obter_restaurantes():
    tipo = request.args.get('tipo')
    if tipo == 'italiano':
        restaurantes_italianos = [
            {"id": 4, "nome": "Cantina da Nonna", "tipo": "Italiano", "cidade": "Curitiba"},
            {"id": 5, "nome": "Bella Macarronada", "tipo": "Italiano", "cidade": "São Paulo"}
        ]
        return jsonify(restaurantes_italianos)

    restaurantes = [
        {"id": 1, "nome": "Churrascaria Fogo Forte", "tipo": "Carnes", "cidade": "Cascavel"},
        {"id": 2, "nome": "Sushi Express", "tipo": "Japonês", "cidade": "Londrina"},
        {"id": 3, "nome": "Burger House", "tipo": "Lanches", "cidade": "Maringá"}
    ]
    return jsonify(restaurantes)

@app.route('/restaurantes/<int:id>')
def obter_restaurante_por_id(id):
    restaurante = {"id": id, "nome": "Pizzaria Napoli", "tipo": "Italiano", "cidade": "Quedas do Iguaçu"}
    return jsonify(restaurante)

app.run(debug=True)