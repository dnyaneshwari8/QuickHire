from django.db import models

# Create your models here.


# categories/models.py
class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50)  # bootstrap icon class
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
