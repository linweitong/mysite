from rest_framework import serializers
from vs.models import Place, Video, Comment, VSUser
from django.contrib.auth.models import User
from rest_framework.pagination import PaginationSerializer


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


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'video', 'location', 'geo_latitude', 'geo_longitude', 'creator',
                  'created_date', 'updated_date')


class VCUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = VSUser
        fields = ('id', 'username', 'accessToken')

