from mutantes import mostrar_mutantes, buscar_mutante, adicionar_mutante, remover_mutante, atualizar_mutante, contar_mutante, maior_nivel, media_nivel, filtrar_mutantes, ordenar_mutantes, pegar_grupo 
from utils import pedir_numero, pedir_nivel, pedir_opcao, pedir_quantidade, pedir_texto

def mostrar_menu():
    print('''1 - Mostrar mutantes
2 - Buscar mutante
3 - Adicionar mutante
4 - Remover mutante
5 - Atualizar mutante
6 - Estatísticas
7 - Filtrar
8 - Ordenar
9 - Pegar grupo
10 - Sair
''')

def executar_opcao(opcao):
    if opcao == 1:
        mostrar_mutantes()
    
    elif opcao == 2:
        nome = pedir_texto('Digite o nome do mutante: ')
        resultado = buscar_mutante(nome)
        if resultado:
            print(f"{resultado['nome']} encontrado!")
        else:
            print(f"Mutante não encontrado.")

    elif opcao == 3:
        nome = pedir_texto('Digite o nome do mutante: ')
        resultado = buscar_mutante(nome)
        if resultado:
            print('Mutante já existente.')
            return None
        poder = pedir_texto('Digite o poder: ')
        nivel = pedir_nivel()
        adicionado = adicionar_mutante(nome, poder, nivel)
        print(f"{adicionado['nome']} foi adicionado")
    
    elif opcao == 4:
        nome = pedir_texto('Digite o nome do mutante: ')
        remover = remover_mutante(nome)
        if remover:
            print(f"{remover['nome']} removido.")
        else:
            print(f"Mutante não encontrado.")

    elif opcao == 5:
        nome = pedir_texto('Digite o nome do mutante: ')
        resultado = buscar_mutante(nome)
        if not resultado:
            print('Mutante não existente.')
            return None
        poder = pedir_texto('Digite o poder: ')
        nivel = pedir_nivel()

        mutante_atualizado = atualizar_mutante(nome, poder, nivel)
        if mutante_atualizado:
            print(f"{mutante_atualizado['nome']} foi atualizado.")

    elif opcao == 6:
        quantidade = contar_mutante()
        if quantidade == 0:
            print('Não há nenhum mutante na lista.')
        else:
            maior = maior_nivel()
            media = media_nivel()
            print(f'Quantidade: {quantidade}')
            print(f'Mais forte: {maior["nome"]} - nível {maior["nível"]}')
            print(f'Média de nível: {media:.2f}')

    elif opcao == 7:
        nivel_minimo = pedir_nivel()
        filtrados = filtrar_mutantes(nivel_minimo)
        if filtrados:
            for mutante in filtrados:
                print(f'{mutante["nome"]} - nível {mutante["nível"]}')
        else:
            print('Nenhum mutante encontrado.')

    elif opcao == 8:
        decrescente = ordenar_mutantes()
        if decrescente:
            for mutante in decrescente:
                print(f'{mutante["nome"]} - Poder: {mutante["poder"]} - Nível {mutante["nível"]}')
        else:
            print('Nenhum mutante encontrado.')

    elif opcao == 9:
        quantidade_disponivel = contar_mutante()
        if quantidade_disponivel == 0:
            print('Não há nenhum mutante na lista.')
            return None
        while True:
            quantidade = pedir_quantidade()
            if quantidade > quantidade_disponivel:
                print(f'Só existem {quantidade_disponivel} mutantes disponíveis.')
            else:
                break
        grupo = pegar_grupo(quantidade)
        for mutante in grupo:
            print(f'{mutante["nome"]} - nível {mutante["nível"]}')

    elif opcao == 10:
        print('Saindo do programa...')

def main():
    opcao = 0

    while opcao != 10:
        mostrar_menu()
        opcao = pedir_opcao()
        executar_opcao(opcao)


if __name__ == "__main__":
    main()