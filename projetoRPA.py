from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# service é usado para iniciar uma instância do chrome webdriver
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

url = 'https://quotes.toscrape.com/js-delayed/'
driver.implicitly_wait(15)  # seconds
driver.get(url)


def process_quote_list():
    driver.implicitly_wait(15)  # seconds
    quoteElements = driver.find_elements(
        By.CSS_SELECTOR, 'div#quotesPlaceholder div.quote')
    quoteObjects = []
    for quoteElement in quoteElements:
        quoteObject = process_quote(quoteElement)
        quoteObjects.append(quoteObject)
    print(quoteObjects)


def process_quote(quote):
    textElement = quote.find_element(By.CSS_SELECTOR, 'span.text')
    authorElement = quote.find_element(By.CSS_SELECTOR, 'small.author')
    tags = get_tags(quote)
    return {'text': textElement.text, 'author': authorElement.text, 'tags': tags}


def get_tags(quote):
    tagElements = quote.find_elements(By.CSS_SELECTOR, 'div.tags a.tag')
    tags = []
    for tagElement in tagElements:
        tags.append(tagElement.text)
    return tags


process_quote_list()
