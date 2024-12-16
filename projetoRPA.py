from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import csv
import pandas as pd
import smtplib


def process_quote_list():
    # Aguardar até 15s para os quotes serem carregados
    driver.implicitly_wait(15)
    # busca elementos div que tem classe quote, que são filhos de uma div com ID quotesPlacesHolder
    quoteElements = driver.find_elements(
        By.CSS_SELECTOR, 'div#quotesPlaceholder div.quote')
    quoteObjects = []

    for quoteElement in quoteElements:  # para cada quoteElement
        # monte um quoteObject com os dados da citação, author e tags
        quoteObject = process_quote(quoteElement)
        # e adicione o quoteObject montado na lista
        quoteObjects.append(quoteObject)
    return quoteObjects


def process_quote(quoteElement):
    # busca o elemento HTML que contém a citação
    textElement = quoteElement.find_element(By.CSS_SELECTOR, 'span.text')
    # busca o elemento HTML que contém o author
    authorElement = quoteElement.find_element(By.CSS_SELECTOR, 'small.author')
    # Obtém a lista de tags em formato de string (text)
    tags = get_tags(quoteElement)
    # Monta o quoteObject para agrupar os dados
    return {'text': textElement.text, 'author': authorElement.text, 'tags': ';'.join(tags)}


def get_tags(quoteElement):
    # Busque o elemento HTML que contém as tags
    tagElements = quoteElement.find_elements(By.CSS_SELECTOR, 'div.tags a.tag')
    tags = []
    for tagElement in tagElements:  # Para cada tagElement
        # adicione o texto contido no HTML da tag em uma lista
        tags.append(tagElement.text)
    return tags

# Essa função foi criada para navegar entre as páginas do site, coletar todas as citações e salva-las em um arquivo


def process_pages():
    # cria uma lista onde serão armazenadas as citações de todas as páginas
    allQuotes = []
    # cria um loop onde só será interrompido quando o botão de NEXT não existir mais
    while (True):
        quotesBypage = process_quote_list()
        allQuotes.extend(quotesBypage)
        # verifica se existe um botão next na página através do css selector, buscando um elemento <a> que é filho de uma 'li' que está dentro da 'ul' que está em uma 'nav'
        nextButtomElements = driver.find_elements(
            By.CSS_SELECTOR, 'nav ul.pager li.next a')
        if nextButtomElements == []:
            break
        else:
            nextButtomElements[0].click()
    # Após sair do loop sava todas as citações em uma arquivo
    create_quotes_file(allQuotes)

# cria o arquivo quotes.csv e grava as citações nele


def create_quotes_file(quotes):
    with open('./quotes.csv', mode="w", newline="", encoding="utf-8") as file:
        # Escreve dicionários no arquivo CSV e define as colunas com base nas chaves do 1 dicionário da lista
        writer = csv.DictWriter(file, fieldnames=quotes[0].keys())
        # Escreve o cabeçalho (nomes das colunas)
        writer.writeheader()
        # Escreve as linhas (dados)
        writer.writerows(quotes)

# lê as citações do arquivo quotes.csv e as retorna em forma de lista


def read_quotes_from_file():
    quotes = []
    with open('./quotes.csv', mode="r", encoding="utf-8") as file:
        # lê o arquivo linha por linha
        reader = csv.DictReader(file)
        # para cada linha do arquivo o dicionário correspondente é adicionado à lista
        for row in reader:
            quotes.append(dict(row))
    return quotes

# conta o número de citações presentes na lista lida


def get_quote_count(quotes):
    series = pd.Series(quotes)
    return series.count()


def get_recurrent_author(quotes):
    # Extraindo a lista de autores
    authors = [quote['author'] for quote in quotes]
    # Criando uma Series para calcular as ocorrências
    series = pd.Series(authors)
    # Encontrando o autor mais recorrente
    most_recurrent_author = series.value_counts(
    ).idxmax()  # Obtém o índice do maior valor

    return most_recurrent_author

# idenfiticando a tag mais recorrente dentro da lista de citações


def get_recurrent_tag(quotes):
    # acessa o valor da chave tags, separando por ponto e vírgula
    tags = [quote['tags'].split(';') for quote in quotes]
    # cada item da lista original vira uma linha da Serie e com o 'explode' transforma cada elemento da lista em uma nova linha
    series = pd.Series(tags).explode()
    # conta quantas vezes cada tag aparece na "Series"
    most_recurrent_tag = series.value_counts().idxmax()
    return most_recurrent_tag


def start_scraping():
    url = 'https://quotes.toscrape.com/js-delayed/'
    driver.implicitly_wait(15)  # aguardar até 15s para a página ser carregada
    driver.get(url)

    process_pages()
    quotes = read_quotes_from_file()
    print("Quote count: " + str(get_quote_count(quotes)))
    print("Recurrent author: " + get_recurrent_author(quotes))
    print("Recurrent tag: " + get_recurrent_tag(quotes))


load_dotenv()

host = "smtp.gmail.com"
port = "587"
login = os.getenv("EMAIL_USER")
senha = os.getenv("EMAIL_PASSWORD")

server = smtplib.SMTP(host, port)

server.ehlo()
server.starttls()
server.login(login, senha)

corpo = """
Olá, Boa noite! 

Segue anexo com o relatório das citações extraídas. Abaixo se encontra o resumo do relatório:

**Resumo do Relatório:**

* Total de Citações: 100
* Autor Mais Recorrente: Albert Einstein
* Tag mais recorrente: Love

Atenciosamente,
Marcos Vasconcelos
"""
# montando o E-mail
email_recipients = os.getenv("EMAIL_RECIPIENTS").split(",")
email_msg = MIMEMultipart()
email_msg['From'] = login
email_msg['To'] = ", ".join(email_recipients)
email_msg['subject'] = "Desafio - RPA Python"
email_msg.attach(MIMEText(corpo, 'plain'))

# abrindo o arquivo em modo leitura e binary
cam_arquivo = "E:\\Desafio---RPA-Python\\quotes.csv"
attchment = open(cam_arquivo, 'rb')

# lendo o arquivo no modo binario e jogamos codificado em base 64 pois o email é enviado em base 64
att = MIMEBase('application', 'octet-stream')
att.set_payload(attchment.read())
encoders.encode_base64(att)

# adicionando o cabeçalho no tipo anexo de email
att.add_header('content-Disposition', f'attachment; filename = quotes.csv')
attchment.close()

# colocando o anexo no corpo do e-mail
email_msg.attach(att)

# Enviar o email tipo MIME no servidor SMTP
server.sendmail(email_msg['From'], email_recipients, email_msg.as_string())
server.quit()

# service é usado para iniciar uma instância do chrome webdriver
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
start_scraping()
