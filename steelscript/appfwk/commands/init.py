#!/usr/bin/env python

# Copyright (c) 2015 Riverbed Technology, Inc.
#
# This software is licensed under the terms and conditions of the MIT License
# accompanying the software ("License").  This software is distributed "AS IS"
# as set forth in the License.


import os

from steelscript.commands.steel import BaseCommand, console, shell


class Command(BaseCommand):
    help = 'Initialize App Framework project'

    def main(self):
        cwd = os.getcwd()
        if not os.path.exists('manage.py'):
            console('This command must be run inside the project directory to initialize.')
            return

        shell('python manage.py initialize --trace',
              msg='Initializing project using default settings',
              cwd=cwd)
