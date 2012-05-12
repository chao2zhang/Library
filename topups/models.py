# -*- coding: utf-8 -*-
from django.db import models
from members.models import Member

class Topup(models.Model):
    member = models.ForeignKey(Member, related_name='topups')
    amount = models.FloatField()
    create_at = models.DateTimeField(auto_now_add=True, null=False)
    update_at = models.DateTimeField(auto_now=True, null=False)
    def __unicode__(self):
        s = '%s - %.2f' % (self.member.name, self.amount)
        return s
    #def get_absolute_url(self):
    #    return "/topups/%i/show/" % self.id
    def new(self):#新充值时更新会员余额与积分
        m = self.member
        m.balance += self.amount
        m.point += int(self.amount / 2)
        m.save()
    class Meta:
        ordering = ['-create_at']#指定充值记录的默认排序方式为按时间降序