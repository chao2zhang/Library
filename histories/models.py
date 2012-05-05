from django.db import models

# Create your models here.
class History(models.Model):
    content = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now=True)