from django.apps import AppConfig


class MyCustomSignalsConfig(AppConfig):
    name = 'signals'

    def ready(self):
        import signals
