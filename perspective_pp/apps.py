from django.apps import AppConfig


class PerspectivePpConfig(AppConfig):
    name = 'perspective_pp'

    def ready(self):
        print('perspective_pp.ready')
        from .signals import connect
        connect()
