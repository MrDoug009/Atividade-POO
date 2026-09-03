from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/produtos')
def obter_produtos():
    categoria = request.args.get('categoria')
    if categoria:
        produtos_categoria = [
            {"id": 1, "nome": "Mouse", "preco": 50.0, "categoria": "informatica"},
            {"id": 2, "nome": "Teclado", "preco": 100.0, "categoria": "informatica"}
        ]
        return jsonify(produtos_categoria)

    produtos = [
        {"id": 1, "nome": "Mouse", "preco": 50.0, "categoria": "informatica"},
        {"id": 2, "nome": "Teclado", "preco": 100.0, "categoria": "informatica"},
        {"id": 3, "nome": "Caderno", "preco": 20.0, "categoria": "papelaria"}
    ]
    return jsonify(produtos)

@app.route('/produtos/<int:id>')
def obter_produto_por_id(id):
    produto = {"id": id, "nome": "Monitor", "preco": 800.0, "categoria": "informatica"}
    return jsonify(produto)

app.run(debug=True)