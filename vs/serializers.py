from rest_framework import serializers
from vs.models import Place, Comment, VSUser, PlaceVideo
from django.contrib.auth.models import User
from rest_framework.pagination import PaginationSerializer
from django.conf import settings


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class VSUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = VSUser
        fields = ('id', 'name', 'firstName', 'lastName', 'profileImage','email', 'accessToken',)

class VSBasicUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = VSUser
        fields = ('id', 'name', 'firstName', 'lastName', 'profileImage','email',)


class PlaceSerializer(serializers.ModelSerializer):
    type = serializers.Field(source=False)
    creator = VSBasicUserSerializer(read_only=True)
    additionInfo = serializers.CharField(required=False, allow_none=True)

    class Meta:
        model = Place
        fields = ('id', 'name', 'description', 'type', 'location', 'latitude',
                  'longitude', 'additionInfo', 'creator', 'createdDate', 'updatedDate')


class PaginatedPlaceSerializer(PaginationSerializer):
    """
    Serializes page objects of user querysets.
    """
    class Meta:
        object_serializer_class = PlaceSerializer


class PlaceVideoSerializer(serializers.ModelSerializer):
    videoUrl = serializers.SerializerMethodField('getVideoUrl')
    thumbnailUrl = serializers.SerializerMethodField('getThumbnailUrl')
    creator = VSBasicUserSerializer(read_only=True)

    def getVideoUrl(self, obj):
        return settings.MEDIA_BASE_URL + obj.video.url

    def getThumbnailUrl(self, obj):
        return settings.MEDIA_BASE_URL + obj.thumbnail.url

    class Meta:
        model = PlaceVideo
        fields = ('id', 'thumbnailUrl', 'videoUrl', 'creator', 'location', 'latitude', 'longitude',
                  'createdDate', 'updatedDate')

class PaginatedPlaceVideoSerializer(PaginationSerializer):
    """
    Serializes page objects of user querysets.
    """
    class Meta:
        object_serializer_class = PlaceVideoSerializer




class CommentSerializer(serializers.ModelSerializer):
    type = serializers.Field(source=False)
    creator = VSBasicUserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'text', 'type', 'creator', 'createdDate','updatedDate')

class PaginatedCommentSerializer(PaginationSerializer):
    """
    Serializes page objects of user querysets.
    """
    class Meta:
        object_serializer_class = CommentSerializer

