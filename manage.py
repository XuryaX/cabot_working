#!/usr/bin/env python
import os
import sys


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cabot.settings")

    from django.core.management import execute_from_command_line
    print(sys.argv)
    run = True
    if run:
	execute_from_command_line(sys.argv)
	migration = ['manage.py', 'makemigrations']
	execute_from_command_line(migration)

	migrate = ['manage.py', 'migrate']
	execute_from_command_line(migrate)
