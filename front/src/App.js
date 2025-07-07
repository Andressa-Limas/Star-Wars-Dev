import React, { useEffect, useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const API_URL = process.env.REACT_APP_API_URL;
  const [filmes, setFilmes] = useState([]);
  const [pesquisa, setPesquisa] = useState("");
  const [ordem, setOrdem] = useState("1");
  const [personagemSelecionado, setPersonagemSelecionado] = useState(null);

  useEffect(() => {
    const carregarFilmesComPersonagens = async () => {
      const { data: listaFilmes } = await axios.get(`${API_URL}/filmes`);
      const filmesComPersonagens = await Promise.all(
        listaFilmes.map(async (filme) => {
          const { data: personagens } = await axios.get(
            `${API_URL}/filmes/${filme.episode_id}/personagens`
          );
          return { ...filme, personagens };
        })
      );
      setFilmes(filmesComPersonagens);
    };

    carregarFilmesComPersonagens();
  }, []);

  const filmesFiltrados = filmes
    .filter((f) => {
      const termo = pesquisa.toLowerCase();
      const titulo = f.title.toLowerCase();
      const ano = f.release_date.toLowerCase();
      const personagemMatch = f.personagens?.some((p) =>
        p.name.toLowerCase().includes(termo)
      );
      return titulo.includes(termo) || ano.includes(termo) || personagemMatch;
    })
    .sort((a, b) => {
      if (ordem === "2") return a.title.localeCompare(b.title);
      if (ordem === "3") return b.title.localeCompare(a.title);
      return 0;
    });

  const togglePersonagens = async (filmeId) => {
    const atualizados = await Promise.all(
      filmes.map(async (filme) => {
        if (filme.episode_id === filmeId) {
          if (filme.personagensAtivos) {
            const novo = { ...filme };
            delete novo.personagensAtivos;
            return novo;
          } else {
            return { ...filme, personagensAtivos: true };
          }
        }
        return filme;
      })
    );
    setFilmes(atualizados);
  };

  const abrirDetalhesPersonagem = (personagem) => {
    setPersonagemSelecionado(personagem);
  };

  const fecharDetalhesPersonagem = () => {
    setPersonagemSelecionado(null);
  };

  return (
    <div className="container">
      <div className="search-section">
        <input
          type="text"
          placeholder="Pesquisar filmes, ano ou personagem..."
          value={pesquisa}
          onChange={(e) => setPesquisa(e.target.value)}
          className="form-control search-input"
        />
        <select
          value={ordem}
          onChange={(e) => setOrdem(e.target.value)}
          className="form-control select-ordem"
        >
          <option value="1">Relevância</option>
          <option value="2">Nome (A-Z)</option>
          <option value="3">Nome (Z-A)</option>
        </select>
      </div>
      <div className="card-container">
        {filmesFiltrados.length === 0 && (
          <div className="card">
            <div className="card-body">Nenhum filme encontrado.</div>
          </div>
        )}
        {filmesFiltrados.map((filme) => (
          <div className="card" key={filme.episode_id}>
            <img
              src={`https://cdn.worldvectorlogo.com/logos/star-wars-1.svg`}
              alt={filme.title}
              className="card-img"
            />
            <div className="card-body">
              <div className="widget-26-job-title">
                <a href="#">{filme.title}</a>
                <p className="m-0">
                  <span className="employer-name">Episódio {filme.episode_id}</span>{" "}
                  <span className="text-muted time">{filme.release_date}</span>
                </p>
              </div>
              <div className="widget-26-job-info">
                <p>Diretor: {filme.director}</p>
              </div>
              <button
                className="btn btn-sm btn-outline-info mt-2"
                onClick={() => togglePersonagens(filme.episode_id)}
              >
                {filme.personagensAtivos ? "Ocultar" : "Ver personagens"}
              </button>
              <ul className="mt-2">
                {filme.personagensAtivos &&
                  filme.personagens.map((p, idx) => (
                    <li key={idx}>
                      <a href="#" onClick={() => abrirDetalhesPersonagem(p)}>
                        {p.name}
                      </a>
                    </li>
                  ))}
              </ul>
            </div>
          </div>
        ))}
      </div>

      {personagemSelecionado && (
        <div className="modal-overlay" onClick={fecharDetalhesPersonagem}>
          <div className="modal-content" onClick={(e) => e.stopPropagation()}>
            <h3>{personagemSelecionado.name}</h3>
            <img
          src={`https://i.pinimg.com/474x/bb/48/6f/bb486f95614a235cef6f5f3cd1b6b821.jpg`}
              alt={personagemSelecionado.name}
              style={{ width: "150px", borderRadius: "8px", marginBottom: "10px" }}
            />
            <p><strong>Gênero:</strong> {personagemSelecionado.gender}</p>
            <p><strong>Nascimento:</strong> {personagemSelecionado.birth_year}</p>
            <p><strong>Altura:</strong> {personagemSelecionado.height} cm</p>
            <p><strong>Peso:</strong> {personagemSelecionado.mass} kg</p>
            <p><strong>Cor da pele:</strong> {personagemSelecionado.skin_color}</p>
            <button onClick={fecharDetalhesPersonagem}>Fechar</button>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
