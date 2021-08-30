from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    Email=models.CharField(max_length=100)
#    User=models.ForeignKey(User, on_delete=models.CASCADE)
