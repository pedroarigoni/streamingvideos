from django.apps import AppConfig


class VideoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'video'

    def ready(self):
        from .models import Usuario
        import os

        email = os.getenv('EMAIL_ADMIN')
        senha = os.getenv('SENHA_ADMIN')

        usuarios = Usuario.objects.filter(email=email)
        if not usuarios:
            if os.environ.get('ENV') != 'producao':
                return
            Usuario.objects.create_superuser(
                username='admin',
                email=email,
                password=senha,
                is_active=True,
                is_staff=True,
            )
