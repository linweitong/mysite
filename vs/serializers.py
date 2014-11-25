from rest_framework import serializers
from vs.models import Place, Comment, VSUser, PlaceVideo
from django.contrib.auth.models import User
from rest_framework.pagination import PaginationSerializer
from django.conf import settings


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class PlaceSerializer(serializers.ModelSerializer):
    type = serializers.Field(source=False)
    creator = UserSerializer(read_only=True)

    class Meta:
        model = Place
        fields = ('id', 'name', 'description', 'type', 'location', 'geo_latitude',
                  'geo_longitude', 'addition_info', 'creator', 'created_date', 'updated_date')


class PaginatedPlaceSerializer(PaginationSerializer):
    """
    Serializes page objects of user querysets.
    """
    class Meta:
        object_serializer_class = PlaceSerializer


class PlaceVideoSerializer(serializers.ModelSerializer):
    video_url = serializers.SerializerMethodField('get_video_url')
    creator = UserSerializer(read_only=True)

    def get_video_url(self, obj):
        return settings.VIDEO_BASE_URL + obj.video.url

    class Meta:
        model = PlaceVideo
        fields = ('id', 'thumbnail', 'video_url', 'creator', 'location', 'geo_latitude', 'geo_longitude',
                  'created_date', 'updated_date')


class VCUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = VSUser
        fields = ('id', 'username', 'accessToken')

class CommentSerializer(serializers.ModelSerializer):
    type = serializers.Field(source=False)
    creator = UserSerializer(read_only=True)
    video = PlaceVideoSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'text', 'type', 'creator', 'created_date','updated_date','video')


