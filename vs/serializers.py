from rest_framework import serializers
from vs.models import Place, Video, Comment


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('id', 'name', 'description', 'type', 'location', 'geo_latitude',
                  'geo_longitude', 'addition_info', 'creator', 'created_date', 'updated_date')


