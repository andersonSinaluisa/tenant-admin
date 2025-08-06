from django.apps import AppConfig


class TenantsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tenants'

    def ready(self):
        # Import persistence models so Django registers them
        from .infrastructure.persistence import tenant_django_model, contact_django_model, plan_django_model  # noqa
