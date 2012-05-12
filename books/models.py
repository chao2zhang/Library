# -*- coding: utf-8 -*-
from django.db import models

class Book(models.Model):
    isbn = models.CharField(max_length=13)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    press = models.CharField(max_length=200)
    count = models.IntegerField(default=0)
    sale_price = models.FloatField()
    create_at = models.DateTimeField(auto_now_add=True, null=False)
    update_at = models.DateTimeField(auto_now=True, null=False)
    def __unicode__(self):#显示此Book记录的默认格式
        return u'<%s> by %s' % (self.title, self.author)
    def get_absolute_url(self):#显示此记录对应详细信息的url
        return "/books/%i/show/" % self.id
    class Meta:
        ordering = ['-create_at']#指定默认排序方式为时间降序
