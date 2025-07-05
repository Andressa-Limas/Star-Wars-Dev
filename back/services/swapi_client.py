import requests

BASE_URL = "https://swapi.dev/api"

def fetch(endpoint):
    url = f"{BASE_URL}/{endpoint}"
    try:
        response = requests.get(url, timeout=10, verify=False)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        return {"results": []}

def filtro_inclusivo(item, chave, valor):
    if not valor:
        return True
    return valor.lower() in item.get(chave, "").lower()

def buscar_personagens(nome=None, genero=None, planeta=None):
    data = fetch("people/")
    resultados = []
    for p in data["results"]:
        if filtro_inclusivo(p, "name", nome) and filtro_inclusivo(p, "gender", genero):
            resultados.append(p)
    return resultados

def buscar_filmes(titulo=None, ano=None, ordem="asc"):
    data = fetch("films/")
    filmes = [
        f for f in data["results"]
        if filtro_inclusivo(f, "title", titulo)
        and (not ano or f["release_date"].startswith(ano))
    ]
    return sorted(filmes, key=lambda x: x["title"], reverse=(ordem == "desc"))

def buscar_personagens_do_filme(id):
    data = fetch("films/")
    try:
        filme = next(f for f in data["results"] if f["episode_id"] == id)
    except StopIteration:
        return []

    personagens = []
    for url in filme["characters"]:
        try:
            res = requests.get(url, timeout=10, verify=False)
            res.raise_for_status()
            personagens.append(res.json())
        except requests.exceptions.RequestException:
            continue
    return personagens

def buscar_personagem_por_nome(nome):
    if not nome:
        return None
    url = f"{BASE_URL}/people/?search={nome}"
    try:
        response = requests.get(url, timeout=10, verify=False)
        response.raise_for_status()
        dados = response.json()
        return dados["results"][0] if dados["results"] else None
    except requests.exceptions.RequestException:
        return None
