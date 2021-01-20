from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    description = models.CharField(max_length=50)

    def __str__(self):
        return self.description
