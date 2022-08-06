from __future__ import absolute_import, unicode_literals
import sys
from celery import Celery

from django.core.management import call_command
import sys

app = Celery()

@app.task
def bkup():
    sys.stdout = open('db.json', 'w')
    call_command('dumpdata', 'task3')