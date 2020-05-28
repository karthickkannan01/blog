from django.apps import AppConfig


class BlogokConfig(AppConfig):
    name = 'blogok'

    def ready(self):
        import blogok.signals