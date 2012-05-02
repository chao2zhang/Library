# -*- coding: utf-8 -*-
import sys, os
from django.core.management import setup_environ
sys.path.append(os.getcwd())

import settings_copy as settings
setup_environ(settings)

from books.models import Book
from members.models import Member
from sales.models import Sale

t = int(raw_input('number of sales you want to add:'))

import random

def get_rand(s):
    return s[random.randint(0, len(s) - 1)]

books = Book.objects.all()
members = Member.objects.all()

for i in range(t):
    s = Sale()
    s.book = get_rand(books)
    s.member = get_rand(members)
    s.count = random.randint(1, 3)
    if s.book.count < s.count:
        continue
    s.new()
    s.save()
    print s