from django.db import models
from django.contrib.auth.models import User
import time


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
    geo_latitude = models.FloatField()
    geo_longitude = models.FloatField()
    # Json to store additional info
    addition_info = models.TextField(null=True)
    creator = models.ForeignKey('auth.User')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


def file_path(self, filename=None):
    return str.format('%s/%s_%s' %(self.place.id, int(time.time()), str(filename)))

class PlaceVideo(models.Model):

    # video info
    thumbnail = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200)

    # location
    location = models.CharField(max_length=200, null=True)
    geo_latitude = models.FloatField()
    geo_longitude = models.FloatField()

    video = models.FileField(upload_to=file_path)
    creator = models.ForeignKey('auth.User')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    place = models.ForeignKey(Place)


class Comment(models.Model):
    COMMENT_TYPE = (
        (1, 'like'),
        (2, 'comments')
    )
    text = models.TextField(null=True)
    type = models.IntegerField(choices=COMMENT_TYPE)
    creator = models.ForeignKey('auth.User')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    video = models.ForeignKey(PlaceVideo)


class VSUser(User):
    thirdPartId = models.BigIntegerField(null=True)
    thirdPartAccessToken = models.CharField(max_length=400, null=True)
    accessToken = models.CharField(max_length=200, null=True)






