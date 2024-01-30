from django.db import models

# Create your models here.
class Item(models.Model):
    
    item = models.TextField()

    def __str__(self):
        return self.item