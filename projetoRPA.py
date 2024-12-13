from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import csv
import pandas as pd


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
    # busque o elemento HTML que contém a citação
    textElement = quoteElement.find_element(By.CSS_SELECTOR, 'span.text')
    # busque o elemento HTML que contém o author
    authorElement = quoteElement.find_element(By.CSS_SELECTOR, 'small.author')
    # Obtenha a lista de tags em formato de string (text)
    tags = get_tags(quoteElement)
    # Monte o quoteObject para agrupar os dados
    return {'text': textElement.text, 'author': authorElement.text, 'tags': ';'.join(tags)}


def get_tags(quoteElement):
    # Busque o elemento HTML que contém as tags
    tagElements = quoteElement.find_elements(By.CSS_SELECTOR, 'div.tags a.tag')
    tags = []
    for tagElement in tagElements:  # Para cada tagElement
        # adicione o texto contido no HTML da tag em uma lista
        tags.append(tagElement.text)
    return tags


def process_pages():
    allQuotes = []
    while (True):
        quotesBypage = process_quote_list()
        allQuotes.extend(quotesBypage)
        nextButtomElements = driver.find_elements(
            By.CSS_SELECTOR, 'nav ul.pager li.next a')
        if nextButtomElements == []:
            break
        else:
            nextButtomElements[0].click()
    create_quotes_file(allQuotes)


def create_quotes_file(quotes):
    # Todo o bloco = criação do arquivo CSV
    with open('./quotes.csv', mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=quotes[0].keys())

        # Escrever o cabeçalho (nomes das colunas)
        writer.writeheader()

        # Escrever as linhas (dados)
        writer.writerows(quotes)


def read_quotes_from_file():
    quotes = []
    with open('./quotes.csv', mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        # Cada linha será um dicionário
        for row in reader:
            quotes.append(dict(row))
    return quotes


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


def get_recurrent_tag(quotes):
    tags = [quote['tags'].split(';') for quote in quotes]
    series = pd.Series(tags).explode()
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


# service é usado para iniciar uma instância do chrome webdriver
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
start_scraping()
