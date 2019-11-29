from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Locations'
