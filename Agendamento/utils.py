import bcrypt
import logging
import smtplib
from email.message import EmailMessage

#função de hash de Senha
def hash_password(password: str):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

#Checagem do hash da senha
def check_password(password: str, hashed_password: str):
    return bcrypt.checkpw(
        password.encode('utf-8'),
        hashed_password.encode('utf-8')
    )
    

logging.basicConfig(level=logging.INFO)
def send_email(to, subject, body):
    logging.info(f"""
    EMAIL SIMULATION
    To: {to}
    Subject: {subject}
    Body: {body}
    """)
    
def send_email_dev(to, subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = 'no-reply@test.com'
    msg['To'] = to

    with smtplib.SMTP('localhost', 1025) as server:
        server.send_message(msg)