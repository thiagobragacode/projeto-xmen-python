import json
from pathlib import Path

ARQUIVO_MUTANTES = Path(__file__).resolve().parent / "mutantes.json"

def carregar_mutantes_de_arquivo(caminho):
    try:
        with open(caminho, "r", encoding="utf-8") as arq:
            return json.load(arq)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def salvar_mutantes_em_arquivo(mutantes, caminho):
    with open(caminho, "w", encoding="utf-8") as arq:
        json.dump(mutantes, arq, ensure_ascii=False, indent=4)

def carregar_mutantes():
    return carregar_mutantes_de_arquivo(ARQUIVO_MUTANTES)


def salvar_mutantes(mutantes):
    salvar_mutantes_em_arquivo(mutantes, ARQUIVO_MUTANTES)


mutantes = carregar_mutantes()

def mostrar_mutantes():
    if not mutantes:
        print("Não há mutantes cadastrados.")
        return

    for mutante in mutantes:
        print(
            f"{mutante['nome']} - "
            f"Poder: {mutante['poder']} - "
            f"Nível: {mutante['nível']}"
        )

def buscar_mutante(nome):       
    for mutante in mutantes:         
        if mutante['nome'].lower() == nome.lower():             
            return mutante     
    return None

def adicionar_mutante(nome, poder, nivel): 
    
    novo_mutante = {
        'nome': nome,
        'poder': poder,
        'nível': nivel
    }
    mutantes.append(novo_mutante)
    salvar_mutantes(mutantes)
    return novo_mutante

def remover_mutante(nome):  
    for mutante in mutantes: 
        if mutante['nome'].lower() == nome.lower(): 
            mutantes.remove(mutante)
            salvar_mutantes(mutantes)  
            return mutante
    return None

def atualizar_mutante(nome, poder, nivel):
    for mutante in mutantes:
        if nome.lower() == mutante['nome'].lower():
            mutante['poder'] = poder
            mutante['nível'] = nivel
            salvar_mutantes(mutantes)
            return mutante
    return None

def contar_mutante():
    return len(mutantes)


def maior_nivel():
    if not mutantes:
        return None

    maior = mutantes[0]

    for mutante in mutantes:
        if mutante['nível'] > maior['nível']:
            maior = mutante

    return maior


def media_nivel():
    if not mutantes:
        return None

    total = 0

    for mutante in mutantes:
        total += mutante['nível']

    media = total / len(mutantes)
    return media

def filtrar_mutantes(nivel_minimo):
    mutantes_filtrados = []
    for mutante in mutantes:
        if mutante['nível'] >= nivel_minimo:
            mutantes_filtrados.append(mutante)
    return mutantes_filtrados

def ordenar_mutantes():
    ordenados = sorted(mutantes, key=lambda x: x["nível"], reverse=True)
    return ordenados

def pegar_grupo(quantidade):
    if quantidade < 0:
        return []

    return mutantes[:quantidade]