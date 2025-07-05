import unittest
from unittest.mock import patch
from app import app

class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch("app.buscar_personagens")
    def test_personagens_sem_filtro(self, mock_buscar):
        mock_buscar.return_value = [{"name": "Luke Skywalker"}]

        response = self.app.get("/personagens")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), [{"name": "Luke Skywalker"}])

    @patch("app.buscar_personagem_por_nome")
    def test_personagem_detalhes_encontrado(self, mock_buscar):
        mock_buscar.return_value = {"name": "Leia Organa"}

        response = self.app.get("/personagens/Leia Organa")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["name"], "Leia Organa")

    @patch("app.buscar_personagem_por_nome")
    def test_personagem_detalhes_nao_encontrado(self, mock_buscar):
        mock_buscar.return_value = None

        response = self.app.get("/personagens/PersonagemInexistente")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json()["erro"], "Personagem não encontrado")

    @patch("app.buscar_filmes")
    def test_filmes_ordenados(self, mock_buscar):
        mock_buscar.return_value = [
            {"title": "A New Hope"},
            {"title": "The Empire Strikes Back"}
        ]

        response = self.app.get("/filmes?ordem=asc")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()), 2)

    @patch("app.buscar_personagens_do_filme")
    def test_personagens_do_filme_encontrado(self, mock_buscar):
        mock_buscar.return_value = [{"name": "Darth Vader"}]

        response = self.app.get("/filmes/4/personagens")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()[0]["name"], "Darth Vader")

    @patch("app.buscar_personagens_do_filme")
    def test_personagens_do_filme_nao_encontrado(self, mock_buscar):
        mock_buscar.return_value = []

        response = self.app.get("/filmes/999/personagens")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json()["erro"], "Filme não encontrado")

    def test_rota_nao_encontrada(self):
        response = self.app.get("/rota-invalida")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json()["erro"], "Rota não encontrada")

if __name__ == "__main__":
    unittest.main()
