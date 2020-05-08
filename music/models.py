from django.db import models

# Create your models here.
class Album(models.Model):
    #year=models.IntegerField()
    pub_name=models.CharField(max_length=100)
    def __str__(self):
        return self.pub_name
class Song(models.Model):

    artist=models.CharField(max_length=100)
    dj=models.CharField(max_length=100)
    album=models.ForeignKey(Album,on_delete=models.CASCADE)
    def __str__(self):
        return self.artist + self.album.pub_name