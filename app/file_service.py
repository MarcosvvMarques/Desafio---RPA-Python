# file_service.py
import csv
from pathlib import Path


def criar_arquivo_citacoes(citacoes, caminho_arquivo='./data/quotes.csv'):
    data_path = Path('./data')
    if not data_path.exists():
        data_path.mkdir()
    with open(caminho_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=citacoes[0].keys())
        escritor.writeheader()
        escritor.writerows(citacoes)


def ler_citacoes_do_arquivo(caminho_arquivo='./data/quotes.csv'):
    data_path = Path('./data')
    if not data_path.exists():
        print('arquivos de citações não encontrado')
        exit(1)
    citacoes = []
    with open(caminho_arquivo, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            citacoes.append(dict(linha))
    return citacoes
