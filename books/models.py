from django.db import models
from django.contrib import admin
from library.members.models import Member
# Create your models here.

class Book(models.Model):
    isbn = models.CharField(max_length=13)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    press = models.CharField(max_length=200)
    count = models.IntegerField()
    sale_price = models.FloatField()
    create_at = models.DateTimeField(auto_now_add=True, null=False)
    update_at = models.DateTimeField(auto_now=True, null=False)
    def __unicode__(self):
        return u'%s : %s' % (self.title, self.author)
    
class Purchase(models.Model):
    book = models.ForeignKey(Book, related_name='purchases')
    price = models.FloatField()
    count = models.IntegerField()
    paid = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True, null=False)
    update_at = models.DateTimeField(auto_now=True, null=False)
    def __unicode__(self):
        return u'%s : %s' % (self.book.title, self.price)

class Sale(models.Model):
    book = models.ForeignKey(Book, related_name='sales')
    member = models.ForeignKey(Member, related_name='sales')
    create_at = models.DateTimeField(auto_now_add=True, null=False)
    update_at = models.DateTimeField(auto_now=True, null=False)
    def __unicode__(self):
        return u'%s : %s' % (self.book.title, self.count)
