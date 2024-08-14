from flask_mail import Mail, Message
from app import app

mail = Mail(app)

def send_email(subject, recipient, body):
    msg = Message(subject, sender=app.config['ALERT_EMAIL'], recipients=[recipient])
    msg.body = body
    mail.send(msg)
