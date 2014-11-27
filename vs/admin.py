from django.contrib import admin
from vs.models import Place, Comment, PlaceVideo, VSUser

admin.site.register(Place)
admin.site.register(PlaceVideo)
admin.site.register(VSUser)
admin.site.register(Comment)
