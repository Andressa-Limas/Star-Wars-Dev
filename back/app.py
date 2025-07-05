from flask import Flask, request, jsonify
from flask_cors import CORS
from flasgger import Swagger, LazyJSONEncoder

app = Flask(__name__)
app.json_encoder = LazyJSONEncoder
CORS(app)
swagger = Swagger(app)

from services.swapi_client import (
    buscar_personagens,
    buscar_filmes,
    buscar_personagens_do_filme,
    buscar_personagem_por_nome
)

@app.route("/personagens", methods=["GET"])
def personagens():
    """
    Lista personagens com filtros opcionais

    ---
    parameters:
      - name: nome
        in: query
        type: string
        required: false
        description: "Nome do personagem para busca parcial"
      - name: genero
        in: query
        type: string
        required: false
        description: "Gênero do personagem (ex: male, female, n/a)"
      - name: planeta
        in: query
        type: string
        required: false
        description: "Planeta natal (não implementado no filtro ainda)"
    responses:
      200:
        description: "Lista de personagens filtrados"
    """
    nome = request.args.get("nome")
    genero = request.args.get("genero")
    planeta = request.args.get("planeta")
    dados = buscar_personagens(nome, genero, planeta)
    return jsonify(dados)

@app.route("/personagens/<nome>", methods=["GET"])
def personagem_detalhes(nome):
    """
    Retorna detalhes de um personagem pelo nome exato

    ---
    parameters:
      - name: nome
        in: path
        type: string
        required: true
        description: "Nome exato do personagem"
    responses:
      200:
        description: "Dados do personagem encontrado"
      404:
        description: "Personagem não encontrado"
    """
    dados = buscar_personagem_por_nome(nome)
    if not dados:
        return jsonify({"erro": "Personagem não encontrado"}), 404
    return jsonify(dados)

@app.route("/filmes", methods=["GET"])
def filmes():
    """
    Lista filmes com filtros opcionais

    ---
    parameters:
      - name: titulo
        in: query
        type: string
        required: false
        description: "Título do filme para busca parcial"
      - name: ano
        in: query
        type: string
        required: false
        description: "Ano de lançamento (ex: 1977)"
      - name: ordem
        in: query
        type: string
        enum:
          - asc
          - desc
        required: false
        default: asc
        description: "Ordem alfabética dos títulos (asc ou desc)"
    responses:
      200:
        description: "Lista de filmes filtrados"
    """
    titulo = request.args.get("titulo")
    ano = request.args.get("ano")
    ordem = request.args.get("ordem", "asc")
    dados = buscar_filmes(titulo, ano, ordem)
    return jsonify(dados)

@app.route("/filmes/<int:id>/personagens", methods=["GET"])
def personagens_do_filme(id):
    """
    Lista personagens de um filme específico pelo ID do episódio

    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: "ID do episódio do filme (ex: 1, 2, 3, ...)"
    responses:
      200:
        description: "Lista de personagens do filme"
      404:
        description: "Filme não encontrado"
    """
    dados = buscar_personagens_do_filme(id)
    if not dados:
        return jsonify({"erro": "Filme não encontrado"}), 404
    return jsonify(dados)

@app.errorhandler(404)
def rota_nao_encontrada(e):
    return jsonify({"erro": "Rota não encontrada"}), 404

@app.errorhandler(500)
def erro_interno(e):
    return jsonify({"erro": "Erro interno do servidor"}), 500

if __name__ == "__main__":
    app.run(debug=True)
