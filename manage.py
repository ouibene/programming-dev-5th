#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "programming.settings.dev") #값을 지정하지 않으면 이 값을 쓰게 되어있음.

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
