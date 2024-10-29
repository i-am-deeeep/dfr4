from django.db import models

# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=30)
    released_on=models.DateField()

    def __str__(self):
        return self.title
