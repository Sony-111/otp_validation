from django.apps import AppConfig

class OtpAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applicatiojn1'  

    def ready(self):
        import applicatiojn1.signals  
