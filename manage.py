#!/usr/bin/env python
import os
import sys


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cabot.settings")

    from django.core.management import execute_from_command_line
    print(sys.argv)
    run = True
    if(len(sys.argv)>=2 and sys.argv[1]=='collectstatic'):
	run = False
	print("Collect Static")
    if run:
	execute_from_command_line(sys.argv)
