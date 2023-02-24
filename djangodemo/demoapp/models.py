from django.db import models


# Create your models here.
class Place(models.Model):
    objects = None
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name


class MeetTheTeam(models.Model):
    objects = None
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='pics')
    detail = models.TextField()

    def __str__(self):
        return self.name
