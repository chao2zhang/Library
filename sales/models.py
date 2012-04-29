from django.db import models
from books.models import Book
from members.models import Member
from groups.models import Group

class Sale(models.Model):
    book = models.ForeignKey(Book, related_name='sales')
    member = models.ForeignKey(Member, related_name='sales', null=True, blank=True)
    count = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True, null=False)
    update_at = models.DateTimeField(auto_now=True, null=False)
    def __unicode__(self):
        return u'%s : %s' % (self.book.title, self.count)
    def get_absolute_url(self):
        return "/sales/%i/show/" % self.id
    
    def new_sale(self):
        discount = self.member.group.discount
        self.book.count -= self.count
        self.member.balance -= discount * self.count * self.book.sale_price
        self.member.save()
        self.book.save()
        