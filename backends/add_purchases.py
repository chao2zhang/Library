# -*- coding: utf-8 -*-
import sys, os
from django.core.management import setup_environ
sys.path.append(os.getcwd())

import settings_copy as settings
setup_environ(settings)

from books.models import Book
from purchases.models import Purchase

t = int(raw_input('number of purchases you want to add:'))

import random

def get_rand(s):
    return s[random.randint(0, len(s) - 1)]

books = Book.objects.all()

for i in range(t):
    p = Purchase()
    p.book = get_rand(books)
    p.count = random.randint(0, 20)
    p.paid = bool(random.randint(0, 1))
    p.price = round(p.book.sale_price * random.random(), 2)
    p.save()
    if p.paid:
        p.paid = False
        p.pay()
    print p
    