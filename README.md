# X-Men — Sistema de Gerenciamento de Mutantes

Projeto desenvolvido em Python para praticar lógica de programação, organização de código, manipulação de arquivos JSON, testes automatizados e controle de versão com Git.

O sistema funciona pelo terminal e permite cadastrar e gerenciar mutantes, armazenando seus nomes, poderes e níveis.

## Funcionalidades

* **Listar mutantes:** exibe todos os mutantes cadastrados.
* **Buscar mutantes:** pesquisa pelo nome, sem diferenciar letras maiúsculas e minúsculas.
* **Adicionar mutantes:** cadastra novos mutantes com nome, poder e nível.
* **Remover mutantes:** exclui mutantes cadastrados.
* **Atualizar mutantes:** modifica o poder e o nível de um mutante.
* **Estatísticas:** apresenta a quantidade de mutantes, o mutante de maior nível e a média dos níveis.
* **Filtrar mutantes:** exibe os mutantes a partir de um nível mínimo.
* **Ordenar mutantes:** organiza os mutantes por nível, do maior para o menor.
* **Selecionar grupo:** exibe uma quantidade específica de mutantes.
* **Persistência de dados:** salva as alterações em um arquivo JSON, preservando os dados após o encerramento do programa.
* **Validação de entradas:** trata entradas inválidas e impede o cadastro de textos vazios e níveis fora do intervalo permitido.
* **Testes automatizados:** utiliza `pytest` para verificar o comportamento das funcionalidades e o armazenamento dos dados.

## Tecnologias utilizadas

* Python
* JSON
* Pytest
* Git
* GitHub

## Estrutura do projeto

```text
projeto_xmen/
├── main.py
├── mutantes.py
├── mutantes.json
├── utils.py
├── test_mutantes.py
├── .gitignore
└── README.md
```

### Responsabilidade dos arquivos

* `main.py`: apresenta o menu e coordena a execução das funcionalidades.
* `mutantes.py`: contém as operações de gerenciamento, estatísticas, filtros, ordenação e persistência dos dados.
* `mutantes.json`: armazena os mutantes cadastrados.
* `utils.py`: reúne funções de entrada e validação de dados.
* `test_mutantes.py`: contém os testes automatizados.
* `.gitignore`: define os arquivos e diretórios que não devem ser rastreados pelo Git.

## Como executar o projeto

### Pré-requisitos

* Python instalado.
* Git instalado, caso queira clonar o repositório.

### 1. Clone o repositório

```bash
git clone https://github.com/thiagobragacode/projeto-xmen-python.git
```

### 2. Entre na pasta do projeto

```bash
cd projeto-xmen-python
```

### 3. Execute o programa

```bash
python main.py
```

O menu será exibido no terminal. Escolha uma opção e siga as instruções apresentadas.

> Se o comando `python` não funcionar no seu sistema, tente `py main.py` no Windows.

## Como executar os testes

O projeto utiliza `pytest` para verificar o funcionamento das funcionalidades.

Se ainda não tiver o pytest instalado, execute:

```bash
python -m pip install pytest
```

Para executar os testes, utilize:

```bash
python -m pytest -v
```

Os testes verificam comportamentos como busca, cadastro, atualização, remoção, persistência em JSON e tratamento de arquivos ausentes ou inválidos.

**Status atual:** 15 testes automatizados passaram durante o desenvolvimento.

## Objetivos de aprendizagem

Este projeto foi desenvolvido para praticar:

* Funções e modularização em Python.
* Listas e dicionários.
* Estruturas condicionais e laços de repetição.
* Manipulação de arquivos com JSON.
* Tratamento de exceções.
* Validação e tratamento de entradas do usuário.
* Testes automatizados com `pytest`.
* Versionamento de código com Git e GitHub.

## Possíveis melhorias futuras

* Criar uma interface web com Flask.
* Substituir o armazenamento em JSON por um banco de dados SQL.
* Desenvolver uma API REST para gerenciar os mutantes.
* Implementar filtros e opções de pesquisa adicionais.

## Autor

**Thiago Braga**

GitHub: [@thiagobragacode](https://github.com/thiagobragacode)
