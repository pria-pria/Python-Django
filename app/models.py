from django.db import models

# Create your models here.

class blog(models.Model):
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=500)
    author=models.CharField(max_length=70)

    def __str__(self):
        return self.title