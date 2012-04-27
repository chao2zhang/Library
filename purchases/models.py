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
        return u'%s : %s' % (self.book.title, self.price)
    def get_absolute_url(self):
        return "/purchases/%i/show/" % self.id