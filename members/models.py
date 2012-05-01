# -*- coding: utf-8 -*-
from django.db import models
from groups.models import Group
from datetime import *

class Member(models.Model):
    GENDER_CHOICES = (
        ('M', u'男'),
        ('F', u'女'),
    )
    GENDER_CHOICES_WITH_EMPTY = (
        ('', u'不限'),
        ('M', u'男'),
        ('F', u'女'),
    )
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=128)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birthday = models.DateField()
    valid_to = models.DateField()
    valid = models.BooleanField()
    identify_number = models.CharField(max_length=18)
    point = models.IntegerField(default=0)
    balance = models.FloatField(default=0)
    group = models.ForeignKey(Group, null=True, blank=True, related_name = 'members')
    create_at = models.DateTimeField(auto_now_add=True, null=False)
    update_at = models.DateTimeField(auto_now=True, null=False)
    def __unicode__(self):
        return u'%s<%s>' % (self.name, self.gender)
    def get_absolute_url(self):
        return "/members/%i/show/" % self.id
    def set_password(self, raw_password):            
        import random
        from django.contrib.auth.models import get_hexdigest
        algo = 'sha1'
        salt = get_hexdigest(algo, str(random.random()), str(random.random()))[:5]
        hsh = get_hexdigest(algo, salt, raw_password)
        self.password = '%s$%s$%s' % (algo, salt, hsh)
    def check_password(self, raw_password):
        from django.contrib.auth.models import check_password
        return check_password(raw_password, self.password)
    def topup(self, amount):
        self.balance += amount
        self.point += int(amount / 2)
        self.save()
    class Meta:
        ordering = ['-create_at']
        