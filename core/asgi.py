import os

DEBUG = bool(os.getenv("DJANGO_DEBUG"))

if DEBUG:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.config")
    os.environ.setdefault("DJANGO_CONFIGURATION", "Local")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.config")
    os.environ.setdefault("DJANGO_CONFIGURATION", "Production")

from configurations.asgi import get_asgi_application  # noqa
application = get_asgi_application()
