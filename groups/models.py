# -*- coding: utf-8 -*-
from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=200)
    discount = models.FloatField()
    create_at = models.DateTimeField(auto_now_add=True, null=False)
    update_at = models.DateTimeField(auto_now=True, null=False)
    def __unicode__(self):
        return u'<%s>' % (self.name)
    def get_absolute_url(self):
        return "/groups/%i/show/" % self.id
    class Meta:
        ordering = ['-create_at']#指定默认排序方式为按生成时间降序