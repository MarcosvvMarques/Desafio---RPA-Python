# email_service.py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

#Montando a estrutura do e-mail
def enviar_email(caminho_arquivo, destinatarios, total_de_citacoes, autor_recorrente, tag_recorrente):
    host = "smtp.gmail.com"
    port = "587"
    login = os.getenv("EMAIL_USER")
    senha = os.getenv("EMAIL_PASSWORD")
    corpo_email = f"""
    Olá,

    Segue anexo com o relatório das citações extraídas. Abaixo se encontra o resumo do relatório:

    **Resumo do Relatório:**

    * Total de Citações: {total_de_citacoes}
    * Autor Mais Recorrente: {autor_recorrente}
    * Tag mais recorrente: {tag_recorrente}

    Atenciosamente,
    Marcos Vasconcelos
    """

    server = smtplib.SMTP(host, port)
    server.ehlo()
    server.starttls()
    server.login(login, senha)

    #Montando o e-mail
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = ", ".join(destinatarios)
    email_msg['subject'] = "Desafio - RPA Python"
    email_msg.attach(MIMEText(corpo_email, 'plain'))

    #Adiciona o anexo ao e-mail
    with open(caminho_arquivo, 'rb') as arquivo_anexo:
        anexo_email = MIMEBase('application', 'octet-stream')
        anexo_email.set_payload(arquivo_anexo.read())
        encoders.encode_base64(anexo_email)
        anexo_email.add_header('content-Disposition',
                               f'attachment; filename = quotes.csv')

        email_msg.attach(anexo_email)

#envia o email
    server.sendmail(email_msg['From'], destinatarios, email_msg.as_string())
    server.quit()
