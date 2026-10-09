def pedir_nivel():
    while True:
        nivel = pedir_numero("Digite o nível (1 a 10): ")
        if nivel < 1 or nivel > 10:
            print("Nível inválido. Digite um valor entre 1 e 10.")
        else:
            return nivel

def pedir_numero(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
            return numero
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

def pedir_opcao():
    while True:
        opcao = pedir_numero("Digite uma opção: ")
        if opcao < 1 or opcao > 10:
            print("Opção inválida. Escolha um número entre 1 e 10.")
        else:
            return opcao

def pedir_quantidade():
    while True:
        numero = pedir_numero("Digite a quantidade de mutantes: ")
        if numero < 1:
            print("A quantidade precisa ser pelo menos 1.")
        else:
            return numero

def pedir_texto(mensagem):
    while True:
        texto = input(mensagem).strip()

        if texto:
            return texto

        print("O texto não pode ficar vazio.")