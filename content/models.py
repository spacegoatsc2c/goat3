from django.db import models

# Create your models here.
class Content(models.Model):
    text = models.TextField(default="")
