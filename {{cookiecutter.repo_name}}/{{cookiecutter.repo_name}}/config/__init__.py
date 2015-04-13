{% if cookiecutter.django_version == "1.8" %}# -*- coding: utf-8 -*-
from __future__ import absolute_import

from .local import Local  # noqa
from .production import Production  # noqa
{% endif %}