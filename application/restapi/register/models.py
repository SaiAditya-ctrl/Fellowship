from django.db import models
from django.utils import timezone
# Create your models here.
class Register(models.Model):
    firstName=models.CharField(max_length=30)
    lastName=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=30)
    desc=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    def __str(self):
        return self.username