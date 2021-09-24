from flask_mail import Message
from . import mail 
from flask import render_template


def mail_message(subject,template,to,**kwargs):
    sender_email = 'jymal6anthony4@gmail.com'
