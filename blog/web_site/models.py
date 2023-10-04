from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название категорий")

    def __str__(self):
        return self.name
