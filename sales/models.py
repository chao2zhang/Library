from django.db import models
from library.books.models import Book
from library.members.models import Member

class Sale(models.Model):
    book = models.ForeignKey(Book, related_name='sales')
    member = models.ForeignKey(Member, related_name='sales', null=True, blank=True)
    count = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True, null=False)
    update_at = models.DateTimeField(auto_now=True, null=False)
    def __unicode__(self):
        return u'%s : %s' % (self.book.title, self.count)
