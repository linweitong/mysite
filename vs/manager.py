from django.db import models
from django.db.models import Count

class LocationManager(models.Manager):

    def byDistance(self, latitude, longitude, excludeEmpty=False):
        """
        Return all object which distance to specified coordinates
        is less than proximity given in kilometers
        """
        # Great circle distance formula
        gcd = """
              6371 * acos(
               cos(radians(%s)) * cos(radians(vs_place.latitude))
               * cos(radians(vs_place.longitude) - radians(%s)) +
               sin(radians(%s)) * sin(radians(vs_place.latitude))
              )
              """
        #gcd_lt = "{} < %s".format(gcd)
        if excludeEmpty:
            return self.get_queryset()\
                   .annotate(videoCount=Count('placeVideos'))\
                   .exclude(videoCount=0)\
                   .exclude(latitude=None)\
                   .exclude(longitude=None)\
                   .extra(
                       select={'distance': gcd},
                       select_params=[latitude, longitude, latitude],
                       #where=[gcd_lt],
                       #params=[latitude, longitude, latitude, proximity],
                       #params=[latitude, longitude, latitude],
                       order_by=['distance']
                   )
        else:
            return self.get_queryset()\
                   .exclude(latitude=None)\
                   .exclude(longitude=None)\
                   .extra(
                       select={'distance': gcd},
                       select_params=[latitude, longitude, latitude],
                       #where=[gcd_lt],
                       #params=[latitude, longitude, latitude, proximity],
                       #params=[latitude, longitude, latitude],
                       order_by=['distance']
                   )


    def searchPlace(self, latitude, longitude, ):
         # Great circle distance formula
        gcd = """
              6371 * acos(
               cos(radians(%s)) * cos(radians(vs_place.latitude))
               * cos(radians(vs_place.longitude) - radians(%s)) +
               sin(radians(%s)) * sin(radians(vs_place.latitude))
              )
              """

        gcd_lt = "{} < %s".format(gcd)
        return self.get_queryset()\
                   .exclude(latitude=None)\
                   .exclude(longitude=None)\
                   .extra(
                       select={'distance': gcd},
                       select_params=[latitude, longitude, latitude],
                       where=[gcd_lt],
                       params=[latitude, longitude, latitude, 0.5],
                       order_by=['distance']
                   )





class PlaceVideoManager(models.Manager):
    def with_counts(self):
        selectViewCount = """
              SELECT COUNT(*) FROM vs_comment WHERE vs_comment.video_id = vs_placevideo.id and vs_comment.type = 3
              """
        return self.get_queryset()\
                   .extra(
                    select={'viewCount':selectViewCount }
                   ).order_by('-updatedDate')