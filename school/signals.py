from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

from .models import Student


@receiver(post_save, sender=Student)
def send_student_created_email(sender, instance, created, **kwargs):
    if created:
        subject = "New Student Created"
        message = f"A new student, {instance.full_name}, has been created."
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [instance.email]
        send_mail(subject, message, from_email, recipient_list)
