from django.db import models
from django.contrib.auth.models import User
import time


class VSUser(User):
    thirdPartId = models.BigIntegerField(null=True)
    thirdPartAccessToken = models.CharField(max_length=400, null=True)
    accessToken = models.CharField(max_length=200, null=True)
    firstName = models.CharField(max_length=200, null=True)
    lastName = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    profileImage = models.CharField(max_length=200, null=True)

class Place(models.Model):
    PLACE_TYPE = (
        (1, 'Club'),
        (2, 'Coffee')
    )

    name = models.CharField(max_length=200)
    description = models.TextField()
    type = models.IntegerField(choices=PLACE_TYPE)
    # location
    location = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    # Json to store additional info
    additionInfo = models.TextField(null=True, blank=True)
    creator = models.ForeignKey(VSUser)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


def thumbnail_path(self, filename=None):
    return str.format('%s/thumbnails/%s_%s' %(self.place.id, int(time.time()), str(filename)))

def video_path(self, filename=None):
    return str.format('%s/videos/%s_%s' %(self.place.id, int(time.time()), str(filename)))

class PlaceVideo(models.Model):

    # video info
    thumbnail = models.FileField(upload_to=thumbnail_path)
    description = models.CharField(max_length=200)

    # location
    location = models.CharField(max_length=200, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    video = models.FileField(upload_to=video_path)
    creator = models.ForeignKey(VSUser)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)
    place = models.ForeignKey(Place)


class Comment(models.Model):
    COMMENT_TYPE = (
        (1, 'like'),
        (2, 'comments')
    )
    text = models.TextField(null=True)
    type = models.IntegerField(choices=COMMENT_TYPE)
    creator = models.ForeignKey(VSUser)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)
    video = models.ForeignKey(PlaceVideo)









