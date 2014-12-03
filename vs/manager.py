from django.db import models

class LocationManager(models.Manager):
    def byDistance(self, latitude, longitude):
        """
        Return all object which distance to specified coordinates
        is less than proximity given in kilometers
        """
        # Great circle distance formula
        gcd = """
              6371 * acos(
               cos(radians(%s)) * cos(radians(latitude))
               * cos(radians(longitude) - radians(%s)) +
               sin(radians(%s)) * sin(radians(latitude))
              )
              """
        #gcd_lt = "{} < %s".format(gcd)
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
