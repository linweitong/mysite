from django.conf.urls import patterns, include, url
from vs import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',
    url(r'^places/$', views.PlaceList.as_view()),
    url(r'^places/(?P<pk>[0-9]+)/$', views.PlaceDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)