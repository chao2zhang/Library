# -*- coding: utf-8 -*-
import sys, os
from django.core.management import setup_environ
sys.path.append(os.getcwd())

import settings_copy as settings
setup_environ(settings)

from members.models import Member
from groups.models import Group

t = int(raw_input('number of members you want to add:'))

import random, datetime

NAME_PREFIX = u'赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜'
NAME_SUFFIX = u'伟芳秀敏杰丹灵华兆婷超梁晗辉军越征凯腾江帆一中君盛丽群来未晨和刚明娜'

def get_rand(s):
    return s[random.randint(0, len(s) - 1)]

groups = Group.objects.all()

for i in range(t):
    m = Member()
    m.balance = round(random.random() * 1000)
    m.birthday = datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 30000))
    m.gender = get_rand(('M', 'F'))
    m.group = get_rand(groups)
    m.identify_number = round(random.random() * (10 ** 18))
    m.name = get_rand(NAME_PREFIX) + get_rand(NAME_SUFFIX);
    if random.randint(0, 2) == 1:
        m.name += get_rand(NAME_SUFFIX)
    m.point = random.randint(0, 200)
    m.valid = bool(random.randint(0, 1))
    m.valid_to = datetime.datetime.now() + datetime.timedelta(days=random.randint(0, 1000))
    m.set_password('naiziylx')
    m.save()
    print m