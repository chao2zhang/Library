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
    def __unicode__(self):
        return u'<%s> by %s' % (self.title, self.author)
    def get_absolute_url(self):
        return "/books/%i/show/" % self.id
    class Meta:
        ordering = ['-create_at']
    
    
