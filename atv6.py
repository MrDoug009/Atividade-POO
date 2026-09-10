from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/carros')
def obter_carros():
    marca = request.args.get('marca')
    if marca == 'toyota':
        carro_toyota = [{"id": 4, "modelo": "Corolla", "marca": "Toyota", "ano": 2022}]
        return jsonify(carro_toyota)

    carros = [
        {"id": 1, "modelo": "Civic", "marca": "Honda", "ano": 2021},
        {"id": 2, "modelo": "Onix", "marca": "Chevrolet", "ano": 2020},
        {"id": 3, "modelo": "HB20", "marca": "Hyundai", "ano": 2023}
    ]
    return jsonify(carros)

@app.route('/carros/<int:id>')
def obter_carro_por_id(id):
    carro = {"id": id, "modelo": "Hilux", "marca": "Toyota", "ano": 2024}
    return jsonify(carro)

app.run(debug=True)