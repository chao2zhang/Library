from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class History(models.Model):
    content = models.CharField(max_length=200)
    unicode = models.CharField(max_length=200)
    url = models.CharField(max_length=200, null=True, blank=True)
    klass = models.CharField(max_length=20)
    user = models.ForeignKey(User)
    create_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-create_at']#指定默认排序方式为按时间降序
