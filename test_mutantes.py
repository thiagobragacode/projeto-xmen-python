
import mutantes


def test_buscar_mutante():
    resultado = mutantes.buscar_mutante("Wolverine")

    assert resultado is not None
    assert resultado["nome"] == "Wolverine"


def test_buscar_mutante_sem_diferenciar_maiusculas():
    resultado = mutantes.buscar_mutante("wOLVERINE")

    assert resultado is not None
    assert resultado["nome"] == "Wolverine"


def test_buscar_mutante_inexistente():
    resultado = mutantes.buscar_mutante("Deadpool")

    assert resultado is None


def test_adicionar_mutante(monkeypatch):
    lista_teste = []

    monkeypatch.setattr(mutantes, "mutantes", lista_teste)
    monkeypatch.setattr(mutantes, "salvar_mutantes", lambda lista: None)

    resultado = mutantes.adicionar_mutante(
        "Noturno",
        "Teletransporte",
        7
    )

    assert resultado["nome"] == "Noturno"
    assert resultado["poder"] == "Teletransporte"
    assert resultado["nível"] == 7
    assert len(lista_teste) == 1


def test_atualizar_mutante(monkeypatch):
    lista_teste = [
        {
            "nome": "Gambit",
            "poder": "Energia cinética",
            "nível": 7
        }
    ]

    monkeypatch.setattr(mutantes, "mutantes", lista_teste)
    monkeypatch.setattr(mutantes, "salvar_mutantes", lambda lista: None)

    resultado = mutantes.atualizar_mutante(
        "Gambit",
        "Manipulação cinética",
        9
    )

    assert resultado["poder"] == "Manipulação cinética"
    assert resultado["nível"] == 9
    assert lista_teste[0]["nível"] == 9


def test_remover_mutante(monkeypatch):
    lista_teste = [
        {
            "nome": "Noturno",
            "poder": "Teletransporte",
            "nível": 7
        }
    ]

    monkeypatch.setattr(mutantes, "mutantes", lista_teste)
    monkeypatch.setattr(mutantes, "salvar_mutantes", lambda lista: None)

    resultado = mutantes.remover_mutante("Noturno")

    assert resultado["nome"] == "Noturno"
    assert len(lista_teste) == 0


def test_atualizar_mutante_inexistente(monkeypatch):
    lista_teste = [
        {
            "nome": "Gambit",
            "poder": "Energia cinética",
            "nível": 7
        }
    ]

    monkeypatch.setattr(mutantes, "mutantes", lista_teste)
    monkeypatch.setattr(mutantes, "salvar_mutantes", lambda lista: None)

    resultado = mutantes.atualizar_mutante(
        "Deadpool",
        "Fator de cura",
        10
    )

    assert resultado is None
    assert len(lista_teste) == 1
    assert lista_teste[0]["nome"] == "Gambit"


def test_remover_mutante_inexistente(monkeypatch):
    lista_teste = [
        {
            "nome": "Gambit",
            "poder": "Energia cinética",
            "nível": 7
        }
    ]

    monkeypatch.setattr(mutantes, "mutantes", lista_teste)
    monkeypatch.setattr(mutantes, "salvar_mutantes", lambda lista: None)

    resultado = mutantes.remover_mutante("Deadpool")

    assert resultado is None
    assert len(lista_teste) == 1
    assert lista_teste[0]["nome"] == "Gambit"


def test_salvar_e_carregar_mutantes(tmp_path):
    arquivo_teste = tmp_path / "mutantes_teste.json"

    lista_teste = [
        {
            "nome": "Jean Grey",
            "poder": "Telepatia",
            "nível": 10
        }
    ]

    mutantes.salvar_mutantes_em_arquivo(lista_teste, arquivo_teste)
    resultado = mutantes.carregar_mutantes_de_arquivo(arquivo_teste)

    assert resultado == lista_teste


def test_maior_nivel_lista_vazia(monkeypatch):
    monkeypatch.setattr(mutantes, "mutantes", [])

    assert mutantes.maior_nivel() is None


def test_media_nivel_lista_vazia(monkeypatch):
    monkeypatch.setattr(mutantes, "mutantes", [])

    assert mutantes.media_nivel() is None


def test_carregar_arquivo_inexistente(tmp_path):
    caminho = tmp_path / "nao_existe.json"

    resultado = mutantes.carregar_mutantes_de_arquivo(caminho)

    assert resultado == []


def test_carregar_json_invalido(tmp_path):
    caminho = tmp_path / "invalido.json"
    caminho.write_text("{ json inválido", encoding="utf-8")

    resultado = mutantes.carregar_mutantes_de_arquivo(caminho)

    assert resultado == []


def test_remocao_persistida_no_json(tmp_path, monkeypatch):
    caminho = tmp_path / "mutantes_teste.json"

    lista_teste = [
        {"nome": "Gambit", "poder": "Manipulação cinética", "nível": 9},
        {"nome": "Noturno", "poder": "Teletransporte", "nível": 7}
    ]

    mutantes.salvar_mutantes_em_arquivo(lista_teste, caminho)

    monkeypatch.setattr(mutantes, "mutantes", lista_teste)
    monkeypatch.setattr(
        mutantes,
        "salvar_mutantes",
        lambda lista: mutantes.salvar_mutantes_em_arquivo(lista, caminho)
    )

    resultado = mutantes.remover_mutante("Noturno")

    mutantes_recarregados = mutantes.carregar_mutantes_de_arquivo(caminho)

    assert resultado["nome"] == "Noturno"
    assert len(mutantes_recarregados) == 1
    assert mutantes_recarregados[0]["nome"] == "Gambit"


def test_atualizacao_persistida_no_json(tmp_path, monkeypatch):
    caminho = tmp_path / "mutantes_teste.json"

    lista_teste = [
        {"nome": "Gambit", "poder": "Energia cinética", "nível": 7}
    ]

    mutantes.salvar_mutantes_em_arquivo(lista_teste, caminho)

    monkeypatch.setattr(mutantes, "mutantes", lista_teste)
    monkeypatch.setattr(
        mutantes,
        "salvar_mutantes",
        lambda lista: mutantes.salvar_mutantes_em_arquivo(lista, caminho)
    )

    resultado = mutantes.atualizar_mutante(
        "Gambit",
        "Manipulação cinética",
        9
    )

    mutantes_recarregados = mutantes.carregar_mutantes_de_arquivo(caminho)

    assert resultado["poder"] == "Manipulação cinética"
    assert resultado["nível"] == 9
    assert mutantes_recarregados[0]["poder"] == "Manipulação cinética"
    assert mutantes_recarregados[0]["nível"] == 9