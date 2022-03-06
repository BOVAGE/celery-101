from django.template import context
from django.conf import settings
from django.template.loader import render_to_string
from  django.core.mail import send_mail

def send_review_email(name, email, review):
    context = {'name': name, 'email': email, 'review': review}
    email_subject = 'Thank you for the review!'
    email_body = render_to_string('app2/email_template.txt', context)

    return send_mail(
        email_subject,
        email_body,
        settings.DEFAULT_FROM_EMAIL,
        [email],
        fail_silently=False,
        )