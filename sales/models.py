from django.db import models
from books.models import Book
from members.models import Member

class Sale(models.Model):
    book = models.ForeignKey(Book, related_name='sales')
    member = models.ForeignKey(Member, related_name='sales', null=True, blank=True)
    count = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True, null=False)
    update_at = models.DateTimeField(auto_now=True, null=False)
    def __unicode__(self):
        return u'%s * %s -> %s' % (self.book.title, self.count, self.member.name if self.member else 'Anonymous')
    def get_absolute_url(self):
        return "/sales/%i/show/" % self.id
    def new(self):#新交易时更新书库存量和会员余额积分
        member = self.member
        book = self.book
        if member and member.group:
            discount = self.member.group.discount
        else:
            discount = 1
        book.count -= self.count
        if member:
            member.balance -= discount * self.count * book.sale_price
            member.point += self.count * book.sale_price
            member.save()
        book.save()
        return self
    class Meta:
        ordering = ['-create_at']#指定交易记录的默认排序方式为时间降序
        