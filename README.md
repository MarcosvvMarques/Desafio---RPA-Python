# Desafio---RPA-Python 

Este projeto consiste em realizar web scraping em um site para coletar citações, seus autores e as tags associadas a cada um. O script utiliza as bibliotecas Pandas, Selenium e CSV para navegar, coletar dados e analisá-los. Por fim, foi automatizado o envio dos dados extraídos por e-mail atráves da biblioetca smtplib. 

## Pré-requisitos: 

🔹 Antes de rodar o projeto, instale as dependências necessárias: 
🔹 pip install -r requirements.txt 

- O arquivo requirementes.txt deve conter as seguintes bibliotecas: Selenium, pandas e python-dotenv

## Configuração do E-mail:
🔹As credenciais de e-mail e os destinatários do e-mail são armazenados em um arquivo .env, que  tem o seguinte formato:

EMAIL_USER=seu_email@gmail.com
EMAIL_PASSWORD=sua_senha_de_email
EMAIL_RECIPIENTS=email1@example.com,email2@example.com


## Instruções de execução:

1 - Crie o arquivo .env com as suas credenciais de e-mail e instale as dependências com pip install -r requirements.txt

2 - Execute o arquivo main.py para iniciar o processo de scraping e envio do e-mail: python ./app/main.py 

- Após a execução será possível: 

🔹Realizar o scraping das citações;
🔹Salvar as citações em quotes.csv;
🔹Calcular o número de citações, autor mais recorrente e tag mais recorrente;
🔹Enviar um e-mail com o resumo do relatório e o arquivo quotes.csv anexado.


## Funcionalidades:

**Web Scraping**: Coleta citações de um site específico (https://quotes.toscrape.com/js-delayed/), processa as informações (texto, autor e tags), e as armazena em um arquivo CSV.

**Envio de E-mail**: Envia um e-mail com o relatório gerado, incluindo um resumo das citações, e anexa o arquivo CSV com as citações extraídas.

**Análise de Dados**: Calcula o número total de citações, identifica o autor mais recorrente e a tag mais recorrente.

## Explicação do Código

**scraping_service.py**
- Esse módulo contém as funções relacionadas ao processo de web scraping:

🔹processar_lista_de_citacoes: Coleta todas as citações de uma página;
🔹processar_citacao: Extrai os dados de uma citação (texto, autor, tags);
🔹obter_tags: Obtém as tags associadas a uma citação;
🔹processar_paginas: Navega entre as páginas de citações e coleta todas as citações.

**file_service.py**
- Esse módulo lida com as operações de leitura e escrita no arquivo CSV:

🔹criar_arquivo_citacoes: Cria um arquivo CSV com as citações extraídas;
🔹ler_citacoes_do_arquivo: Lê o arquivo CSV e retorna uma lista com as citações.

**email_service.py**
🔹Esse módulo é responsável pelo envio de e-mails com o arquivo de citações como anexo (CSV)

**data_service.py**
🔹Esse módulo Contém funções auxiliares, como contagem de citações, identificação do autor mais recorrente e a tag mais recorrente:

contar_citacoes: Conta o número total de citações.
obter_autor_mais_recorrente: Identifica o autor mais recorrente.
obter_tag_mais_recorrente: Identifica a tag mais recorrente.


## Estrutura do Projeto 

🔹 Projeto RPA - Pasta principal do projeto onde estão separados por arquivos todas as funções, arquivo .env, .env.example e requirements.txt;

🔹.env - Arquivo dos dados sensíveis (credenciais de e-mail e senhas);

🔹main.py - Arquivo principal para realizar a execução do script;

🔹scraping_service.py - Módulo para web scraping e extração de dados;

🔹file_service.py - Módulo para manipulação de arquivos (CSV);

🔹email_service.py - Módulo para enviar os e-mails;

🔹data_service.py - Funções auxiliares para o projeto;

🔹quotes.csv - Arquivo gerado com as citações extraídas;

🔹README.md - este arquivo de documentação.










