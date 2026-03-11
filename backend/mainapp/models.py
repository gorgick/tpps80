from django.db import models


class DataJson(models.Model):
    name = models.CharField(max_length=50)
    data = models.DateTimeField()

    def __str__(self):
        return self.name
