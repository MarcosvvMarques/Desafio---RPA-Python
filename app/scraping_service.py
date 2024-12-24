# scraping_service.py
from selenium.webdriver.common.by import By

def processar_lista_de_citacoes(driver):
    driver.implicitly_wait(15)
    elementos_citacoes = driver.find_elements(
        By.CSS_SELECTOR, 'div#quotesPlaceholder div.quote')
    lista_citacoes = []

    for elemento_citacao in elementos_citacoes:
        objeto_citacao = processar_citacao(elemento_citacao)
        lista_citacoes.append(objeto_citacao)
    return lista_citacoes


def processar_paginas(driver):
    todas_as_citacoes = []
    while True:
        citacoes_por_pagina = processar_lista_de_citacoes(driver)
        todas_as_citacoes.extend(citacoes_por_pagina)
        elementos_botao_proximo = driver.find_elements(
            By.CSS_SELECTOR, 'nav ul.pager li.next a')
        if not elementos_botao_proximo:
            break
        else:
            elementos_botao_proximo[0].click()
    return todas_as_citacoes


def processar_citacao(elemento_citacao):
    elemento_texto = elemento_citacao.find_element(
        By.CSS_SELECTOR, 'span.text')
    elemento_autor = elemento_citacao.find_element(
        By.CSS_SELECTOR, 'small.author')
    tags = obter_tags(elemento_citacao)
    return {'texto': elemento_texto.text, 'autor': elemento_autor.text, 'tags': ';'.join(tags)}


def obter_tags(elemento_citacao):
    elementos_tags = elemento_citacao.find_elements(
        By.CSS_SELECTOR, 'div.tags a.tag')
    tags = []
    for elemento_tag in elementos_tags:
        tags.append(elemento_tag.text)
    return tags
