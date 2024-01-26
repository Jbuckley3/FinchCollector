from django.db import models

# Create your models here.

from django.db import models

class Finch(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    size = models.CharField(max_length=255)

    def __str__(self):
        return self.name