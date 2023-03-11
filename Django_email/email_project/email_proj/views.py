from django.http import HttpResponse
import traceback
from django.core.mail import send_mail
from django.template import loader


def index(request):
    # inject the respective values in HTML template
    html_message = loader.render_to_string(
        'email_proj/message.html',
        {
            'name': 'Recipient Name',
            'body': 'Vous avez reçu ce prestigieux email !',
        })
    send_mail(
        'Felicitation !',
        'Vous avez de la chance de recevoir ce courrier.',
        'dollarbilly503@gmail.com',  # Update this with your mail id
        ['sibyamara95@gmail.com', 'dollarbilly503@gmail.com'],  # Update this with the recipients mail id
        html_message=html_message,
        fail_silently=False,
    )

    return HttpResponse("<p>Message envoyer avec succes!!</p>")
