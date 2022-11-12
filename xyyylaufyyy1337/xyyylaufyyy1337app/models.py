from django.db import models

# Create your models here.
class Write(models.Model):
    writer = models.CharField(max_length=100)
    bio = models.TextField('Bio')

    def __str__(self):
        return self.writer