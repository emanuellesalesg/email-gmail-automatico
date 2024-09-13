import smtplib
import email.message

def enviar_email():
    corpo_email = """
    <p>Mensagem 1</p>
    <p>Mensagem 2</p>
"""

    #Definição do assunto
    msg = email.message.Message()
    msg['Subject'] = 'subject'
    msg['From'] = 'email'
    msg['To'] = 'email'
    password = 'password'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    #Logando no email para enviar
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

enviar_email()