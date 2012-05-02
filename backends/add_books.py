# -*- coding: utf-8 -*-
import sys, os
from django.core.management import setup_environ
sys.path.append(os.getcwd())

import settings_copy as settings
setup_environ(settings)

from books.models import Book

t = int(raw_input('number of books you want to add:'))

import random

TITLE_PREFIX = (u'数学', u'方程', u'化学', u'生物', u'疾病', u'神经', u'物理', u'逻辑', u'算法', u'程序', u'数据库', u'网络', u'计算机')
TITLE_SUFFIX = (u'引论', u'概论', u'方法', u'教程', u'导读', u'分析')
AUTHOR_PREFIX = u'赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜'
AUTHOR_SUFFIX = u'伟芳秀敏杰丹灵华兆婷超梁晗辉军越征凯腾江帆一中君盛丽群来未晨和刚明娜'

def get_rand(s):
    return s[random.randint(0, len(s) - 1)]

for i in range(t):
    b = Book()
    b.isbn = str(int(random.random() * (10 ** 13)))
    t = random.randint(1, 2)
    s = ''.join([get_rand(TITLE_PREFIX) for tt in range(0, t)])
    s += get_rand(TITLE_SUFFIX)
    b.title = s
    b.author = get_rand(AUTHOR_PREFIX) + get_rand(AUTHOR_SUFFIX);
    if random.randint(0, 2) == 1:
        b.author += get_rand(AUTHOR_SUFFIX)
    b.press = get_rand((u"复旦大学出版社", u"机械工业出版社", u"中华书局"))
    b.sale_price = round(random.random() * 100) + 1
    print b
    b.save()