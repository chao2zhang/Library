from django.db import models
from django.contrib import admin

class Group(models.Model):
    name = models.CharField(max_length=200)
    discount = models.FloatField()
    create_at = models.DateTimeField(auto_now_add=True, null=False)
    update_at = models.DateTimeField(auto_now=True, null=False)
    def __unicode__(self):
        return u'%s : %s' % (self.id, self.name)

class Member(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=128)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birthday = models.DateField()
    valid_to = models.DateField()
    valid = models.BooleanField()
    identify_number = models.CharField(max_length=18)
    point = models.IntegerField()
    balance = models.FloatField()
    group = models.ForeignKey(Group, related_name = 'members')
    create_at = models.DateTimeField(auto_now_add=True, null=False)
    update_at = models.DateTimeField(auto_now=True, null=False)
    def __unicode__(self):
        return u'%s : %s' % (self)
    