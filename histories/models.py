from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class History(models.Model):
    content = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    create_at = models.DateTimeField(auto_now=True)
