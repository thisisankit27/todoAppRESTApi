from django.db import models

# Create your models here.

class Task(models.Model):
    priority = models.IntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)