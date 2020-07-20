import logging
from time import sleep
from django.core.mail import send_mail
from bullerin_board.celery import app


@app.task
def send_verification_email(email, message):
    sleep(2)
    print("hi")
    send_mail(
        'Новое сообщение',
        (message + 'отправитель: ' + email),
        'from@example.com',
        ['john@example.com',],
    )
    pass
