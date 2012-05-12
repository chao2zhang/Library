# -*- coding: utf-8 -*-
from django.db import models
from books.models import Book

class Purchase(models.Model):
    book = models.ForeignKey(Book, related_name='purchases')
    price = models.FloatField()
    count = models.IntegerField()
    paid = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True, null=False)
    update_at = models.DateTimeField(auto_now=True, null=False)
    def __unicode__(self):
        s = '%s * %s(%s)' % (self.book.title, self.count, self.price)
        if not self.paid:
            s += u'[未支付]'
        return s
    def get_absolute_url(self):
        return "/purchases/%i/show/" % self.id
    def pay(self):#执行支付后对书库存量进行更改
        if not self.paid:
            self.paid = True
            self.save()
            self.book.count += self.count
            self.book.save()
    class Meta:
        ordering = ['paid', '-create_at']#指定默认排序方式为未支付优先，按时间降序