from flask_mail import Message
from flask import render_template
from . import mail

def mail_message(subject,templates,to,**kwargs):
    sender_email = 'immoringa@gmail.com'

    email = Message(subject, sender=sender_email, recipients=[to])
    email.body = render_template(templates + ".txt", **kwargs)
    email.txt = render_template(templates + ".txt", **kwargs)
    mail.send(email)