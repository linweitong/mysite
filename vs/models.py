from django.db import models


class Place(models.Model):
    PLACE_TYPE = (
        (1, 'Club'),
    )

    name = models.CharField(max_length=200)
    description = models.TextField()
    type = models.IntegerField(choices=PLACE_TYPE)
    # location
    location = models.CharField(max_length=200)
    geo_latitude = models.FloatField()
    geo_longitude = models.FloatField()
    # Json to store additional info
    addition_info = models.TextField()
    creator = models.ForeignKey('auth.User', related_name='places')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


class Video(models.Model):
    # video info
    videoThumbnail = models.CharField(max_length=200)
    video = models.FileField()
    # location
    location = models.CharField(max_length=200)
    geo_latitude = models.FloatField()
    geo_longitude = models.FloatField()

    creator = models.ForeignKey('auth.User', related_name='videos')
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
    creator = models.ForeignKey('auth.User', related_name='videos+')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    video = models.ForeignKey(Video)




