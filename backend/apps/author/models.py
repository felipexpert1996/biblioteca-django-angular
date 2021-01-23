from django.db import models

from apps.category.models import Category


class Author(models.Model):
    name = models.CharField(max_length=100)
    category = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.name
