from django_rest_passwordreset.signals import reset_password_token_created
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.db.models.signals import post_save
from django.conf import settings
from .models import User

# -----------------------------
# Password Reset Email
# -----------------------------
@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    # URL to your frontend reset password page
    reset_url = f"http://127.0.0.1:3000/reset-password?token={reset_password_token.key}&uid={reset_password_token.user.pk}"

    # Render HTML with CSS
    email_html_message = render_to_string(
        'email/password_reset.html',
        {
            'reset_url': reset_url,
            'user': reset_password_token.user,
            'css_url': f"http://127.0.0.1:8000/static/email/css/password_reset.css"
        }
    )

    send_mail(
        subject='ZanFinTech Password Reset',
        message='',  # plaintext fallback
        from_email=f'ZanFinTech  LMS <{settings.EMAIL_HOST_USER}>',
        recipient_list=[reset_password_token.user.email],
        html_message=email_html_message,
        fail_silently=False,
    )


# -----------------------------
# Welcome Email on Registration
# -----------------------------
@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        # Render HTML with CSS
        email_html_message = render_to_string(
            'email/welcome.html',
            {
                'user': instance,
                'css_url': f"http://127.0.0.1:8000/static/email/css/welcome.css"
            }
        )

        send_mail(
            subject='Welcome to ZanFintech LMS!',
            message='',  # plaintext fallback
            from_email=f'ZanFintech LMS <{settings.EMAIL_HOST_USER}>',
            recipient_list=[instance.email],
            html_message=email_html_message,
            fail_silently=False,
        )
