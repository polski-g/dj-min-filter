import re

from django import template
from django.conf import settings


register = template.Library()
_rx = r'^(.+)\.([^\.]+)$'


@register.filter
def min(value):
    if settings.DEBUG:
        return value
    matches = re.match(_rx, value)
    if not matches:
        return value
    else:
        return '%s.min.%s' % (matches.group(1), matches.group(2))
