# scraping_service.py
from selenium.webdriver.common.by import By

#Essa função busca elementos na página através do CSS selector e processa cada elemento individualmente retornando uma lista de objetos
def processar_lista_de_citacoes(driver):
    #Aguarda 15s para os quotes e scripts serem carregados
    driver.implicitly_wait(15) 
    #Busca elementos div que tem classe quote, que são filhos de uma div com ID quotesPlaceHolder
    elementos_citacoes = driver.find_elements(By.CSS_SELECTOR, 'div#quotesPlaceholder div.quote')
    lista_citacoes = []

    for elemento_citacao in elementos_citacoes: #Para cada elemento de citação
        objeto_citacao = processar_citacao(elemento_citacao) #Monte um objeto de citação com os dados da citação, autor e tags
        lista_citacoes.append(objeto_citacao) #E é adicionado esse objeto na lista 
    return lista_citacoes

#Função utilizada para navegar entre as páginas do site, coletar as citações e salva-las em um arquivo
def processar_paginas(driver):
    #cria uma lista onde serão armazenadas as citações de todas as páginas
    todas_as_citacoes = []
    #cria um loop onde só será interrompido quando o botão NEXT não existir mais
    while True:
        #coleta as citações de cada página
        citacoes_por_pagina = processar_lista_de_citacoes(driver)
        todas_as_citacoes.extend(citacoes_por_pagina)
        #verifica se há um botão NEXT na página e o CSS procura um elemento <a> que é filho de um 'li' que está dentro de 'ul' que está em uma 'nav'
        elementos_botao_proximo = driver.find_elements(By.CSS_SELECTOR, 'nav ul.pager li.next a')
        if not elementos_botao_proximo:
            break
        else:
            elementos_botao_proximo[0].click()
            #após sair do loop salva todas as citações em um arquivo
    return todas_as_citacoes

#A função abaixo processa e extrai um elemento que dentro dele terá citação, autor e tags
def processar_citacao(elemento_citacao):
    #busca o elemento HTML que contém a citação
    elemento_texto = elemento_citacao.find_element(By.CSS_SELECTOR, 'span.text')
    #busca o elemento HTML que contém o autor
    elemento_autor = elemento_citacao.find_element(By.CSS_SELECTOR, 'small.author')
    #obtém a lista de tags em formato de texto (string)
    tags = obter_tags(elemento_citacao)
    #Monta o objeto de citação para agrupar os dados
    return {'texto': elemento_texto.text, 'autor': elemento_autor.text, 'tags': ';'.join(tags)}

#A função obter_tags foi utilizada para localizar as tags de cada citação e extraí-las para retornar em uma lista
def obter_tags(elemento_citacao):
    #Localiza o elemento HTML que contém as tags
    elementos_tags = elemento_citacao.find_elements(By.CSS_SELECTOR, 'div.tags a.tag')
    tags = []
    for elemento_tag in elementos_tags: #Para cada elemento que contém as tags
        tags.append(elemento_tag.text) #é adicionado o texto da tag em uma lista
    return tags
