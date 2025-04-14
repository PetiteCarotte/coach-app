""" Adaptateur pour les services d'email. """

# pylint: disable=too-few-public-methods, unnecessary-pass

from abc import ABC, abstractmethod

class EmailService(ABC):
    """Interface pour les services d'email."""

    @abstractmethod
    def send_email(self, to, subject, body):
        """ Envoi d'un email """
        pass

class SMTPAdapter(EmailService):
    """Adaptateur pour un service SMTP."""

    def send_email(self, to, subject, body):
        """ Envoi d'un email via SMTP """
        print(f"Envoi via SMTP : {to}, {subject}, {body}")

class SendGridAdapter(EmailService):
    """Adaptateur pour le service SendGrid."""

    def send_email(self, to, subject, body):
        """ Envoi d'un email via SendGrid """
        print(f"Envoi via SendGrid : {to}, {subject}, {body}")
