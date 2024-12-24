# file_service.py
import csv
from pathlib import Path

#cria o arquivo CSV e escreve os dados no arquivo de forma organizada
def criar_arquivo_citacoes(citacoes, caminho_arquivo='./data/quotes.csv'):
    #Adicionei a biblioetca pathlib para garantir que o diretório data esteja disponível antes de realizar operações que dependem dele
    data_path = Path('./data')
    if not data_path.exists():
        data_path.mkdir()
    with open(caminho_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=citacoes[0].keys())
        escritor.writeheader()
        escritor.writerows(citacoes)

#A função abaixo lê os dados do arquivo, transformada cada linha em dicionário e retorna uma lista com os dicionários
def ler_citacoes_do_arquivo(caminho_arquivo='./data/quotes.csv'):
    data_path = Path('./data')
    if not data_path.exists():
        print('arquivos de citações não encontrado')
        exit(1)
    citacoes = []
    with open(caminho_arquivo, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        #Cada linha será um dicionário
        for linha in leitor:
            citacoes.append(dict(linha))
    return citacoes
