from django.conf import settings
from django.templatetags.static import static
from django.urls import reverse
from jinja2 import Environment


def environment(**kwargs):
    env = Environment(**kwargs)
    env.globals.update(
        {
            "settings": settings,
            "static": static,
            "url": reverse,
        }
    )
    return env
