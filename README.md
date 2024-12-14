# Desafio---RPA-Python

Este projeto consiste em realizar web scraping em um site para coletar citações, seus autores e as tags associadas a cada um. O script utiliza as bibliotecas Pandas, Selenium e CSV para navegar, coletar dados e analisá-los. Por fim, foi automatizado o envio dos dados extraídos por e-mail atráves da biblioetca smtplib. 


## Instruções de execução:

1 - Verifique se você tenha o Python instalado em sua máquina. Caso não tenha faça o download por aqui: https://www.python.org/downloads/

2 - Baixe e instale o Visual Studio Code e logo após isso, faça a instalação das biblioetcas selenium utilizando "pip install selenium e Pandas utilizando "pip install pandas". 

3 - Você pode clonar o projeto "https://github.com/MarcosvvMarques/Desafio---RPA-Python.git" e rodá-lo localmente 

4 - Navegue até o diretório do projeto: cd Desafio---RPA-Python

5 - instale as dependências do projeto: pip install -r requirements.txt

6 - Execute o script principal: python projetoRPA.py

7 - Para enviar o E-mail crie um arquivo .env com as chaves "EMAIL_USER" e
"EMAIL_PASSWORD" para que as credenciais fiquem desassociadas ao código


## Dependências

O projeto utiliza as seguintes dependências:

🔹Selenium: Para automação e web scraping;
🔹Pandas: Para manipulação e análise de dados;
🔹CSV: Para leitura e escrita de arquivos CSV.
🔹smtplib: Para enviar por e-mail o arquivo "Quotes.csv",

⚠️ Certifique-se de que todas as dependências estão listadas no arquivo requirements.txt.

## Considerações

- Versão do Navegador: Garanta que a versão do navegador, o Google Chrome e o ChromeDriver estão atualizados e são compatíveis.

- Tempo de Carregamento: O script utiliza implicitly_wait para lidar com tempos de carregamento do site. Certifique-se de que sua conexão é estável.

- Permissões de Rede: O script precisa de acesso à internet para acessar o site a ser raspado.


## Funcionalidades:

🔹 Navegar em todas as páginas de quotes do site;
🔹Coletar e extrair informações sobre as citações, autores e tags;
🔹Salvar os dados coletados em um arquivo CSV;
🔹Ler o arquivo CSV para realizar análises como: Contagem de citações, autor mais recorrente e tag mais frequente. 
🔹 Enviar por e-mail o arquivo quotes.CSV como anexo.

## Tecnologias Utilizadas:

🔹 Linguagem de programação: Python
🔹 Navegador: Google Chrome
🔹 Bibliotecas: Pandas, Selenium, CSV e smtplib. 

## Estrutura do Projeto

🔹 projetoRPA.py: Principal script contendo toda a lógica do web scraping e análise.

🔹quotes.csv: Arquivo gerado com os dados coletados.

🔹requirements.txt: Lista de dependências necessárias para o projeto


