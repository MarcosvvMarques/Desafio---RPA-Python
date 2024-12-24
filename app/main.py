# main.py
from dotenv import load_dotenv
from scraping_service import processar_paginas
from file_service import criar_arquivo_citacoes, ler_citacoes_do_arquivo
from email_service import enviar_email
from data_service import contar_citacoes, obter_autor_mais_recorrente, obter_tag_mais_recorrente
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os


def iniciar_scraping():
    url = 'https://quotes.toscrape.com/js-delayed/'
    driver = webdriver.Chrome(service=Service())
    driver.implicitly_wait(15)  # Aguardar até 15s para a página ser carregada
    driver.get(url)

    citacoes = processar_paginas(driver)
    criar_arquivo_citacoes(citacoes)

    citacoes_lidas = ler_citacoes_do_arquivo()
    total_citacoes = contar_citacoes(citacoes_lidas)
    autor_recorrente = obter_autor_mais_recorrente(citacoes_lidas)
    tag_recorrente = obter_tag_mais_recorrente(citacoes_lidas)

    print("Número de citações: " + str(total_citacoes))
    print("Autor mais recorrente: " + (autor_recorrente))
    print("Tag mais recorrente: " + (tag_recorrente))

    email_destinatarios = os.getenv("EMAIL_RECIPIENTS").split(",")
    caminho_arquivo = './data/quotes.csv'
    enviar_email(caminho_arquivo, email_destinatarios,
                 total_citacoes, autor_recorrente, tag_recorrente)

    driver.quit()


load_dotenv()
iniciar_scraping()
