from django.db import models
from django.contrib.auth.models import User


class Music(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    create_date = models.DateTimeField()
    voter = models.ManyToManyField(User, related_name='voter')



    def __str__(self):
        return f'{self.title} - {self.artist}'


