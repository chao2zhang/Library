# -*- coding: utf-8 -*-
import sys, os
from django.core.management import setup_environ
sys.path.append(os.getcwd())

import settings_copy as settings
setup_environ(settings)

from groups.models import Group

t = int(raw_input('number of groups you want to add:'))

import random

def get_rand(s):
    return s[random.randint(0, len(s) - 1)]

for i in range(t):
    g = Group()
    g.discount = round(random.random(), 2)
    g.name = get_rand(('Super', 'Normal', 'Group')) + str(random.randint(0, 100))
    g.save()
    print g