#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    {% if cookiecutter.django_version == "1.8" %}
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.local")
    from django.core.management import execute_from_command_line
    {% else %}
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config")
    os.environ.setdefault("DJANGO_CONFIGURATION", "Local")

    from configurations.management import execute_from_command_line
    {% endif %}

    execute_from_command_line(sys.argv)
