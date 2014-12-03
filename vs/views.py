from vs.models import Place, VSUser, PlaceVideo, Comment
from vs.serializers import PlaceSerializer, PlaceVideoSerializer, VSUserSerializer, \
    PaginatedPlaceSerializer, CommentSerializer, PaginatedCommentSerializer, PaginatedPlaceVideoSerializer, \
    VSUserVideoSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from urllib2 import urlopen
import json
from django.conf import settings

class PlaceList(APIView):
    """
    List all places, or create a new place.
    """

    # def get(self, request, format=None):
    #     snippets = Place.objects.all()
    #     serializer = PlaceSerializer(snippets, many=True)
    #     return Response(serializer.data)

    def get(self, request, format=None):
        numPerPage = settings.PAGE_NUM

        #places = Place.objects.all()

        #sort places by distance
        latitude = self.request.META.get('HTTP_GEOLATITUDE', 0)
        longitude = self.request.META.get('HTTP_GEOLONGITUDE', 0)
        places = Place.objects.byDistance(latitude,longitude)

        paginator = Paginator(places, numPerPage)
        page = request.QUERY_PARAMS.get('page')
        try:
            places = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            places = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999),
            # deliver last page of results.
            places = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = PaginatedPlaceSerializer(places,
                                         context=serializer_context)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PlaceSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.object.type = 1
            serializer.object.creator = self.request.user
            serializer.save()
            serializer.object.distance = 0
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlaceDetail(APIView):
    """
    Retrieve, update or delete a place instance.
    """

    def get_object(self, pk):
        try:
            latitude = self.request.META.get('HTTP_GEOLATITUDE', 0)
            longitude = self.request.META.get('HTTP_GEOLONGITUDE', 0)
            return Place.objects.byDistance(latitude,longitude).get(pk=pk)

        except Place.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        if int(pk) == 0:
            latitude = self.request.META.get('HTTP_GEOLATITUDE', 0)
            longitude = self.request.META.get('HTTP_GEOLONGITUDE', 0)
            place = Place.objects.byDistance(latitude,longitude)[0]
        else:
            place = self.get_object(pk)
        serializer = PlaceSerializer(place)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        place = self.get_object(pk)
        serializer = PlaceSerializer(place, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        place = self.get_object(pk)
        place.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PlaceVideos(APIView):
    # def get(self, request, placeId, format=None):
    #     placeVideos = PlaceVideo.objects.filter(place_id=placeId)
    #     serializer = PlaceVideoSerializer(placeVideos, many=True)
    #     return Response(serializer.data)

    def get(self, request, placeId, format=None):
        numPerPage = settings.PAGE_NUM
        #placeVideos = PlaceVideo.objects.filter(place_id=placeId)
        placeVideos = PlaceVideo.objects.with_counts().filter(place_id=placeId)
        paginator = Paginator(placeVideos, numPerPage)
        page = request.QUERY_PARAMS.get('page')
        try:
            placeVideos = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            placeVideos = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999),
            # deliver last page of results.
            placeVideos = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = PaginatedPlaceVideoSerializer(placeVideos,
                                         context=serializer_context)

        return Response(serializer.data)

    def post(self, request, placeId, format=None):
        try:
            place = Place.objects.get(pk=placeId)
        except Place.DoesNotExist:
            raise Http404

        placeVideo = PlaceVideo(video=request.FILES['video'], thumbnail=request.FILES['thumbnail'])
        placeVideo.creator = self.request.user
        placeVideo.place = place
        placeVideo.location = place.location
        placeVideo.latitude =self.request.META['HTTP_GEOLATITUDE']
        placeVideo.longitude =self.request.META['HTTP_GEOLONGITUDE']
        placeVideo.save()
        placeVideo.viewCount = 0
        serializer = PlaceVideoSerializer(placeVideo)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



class PlaceVideoDetail(APIView):
    def get(self, request, pk, format=None):
        try:
            placeVideo = PlaceVideo.objects.with_counts().get(pk=pk)
        except PlaceVideo.DoesNotExist:
            raise Http404
        serializer = PlaceVideoSerializer(placeVideo)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        try:
            placeVideo = PlaceVideo.objects.get(pk=pk)
        except PlaceVideo.DoesNotExist:
            raise Http404
        placeVideo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class VideoComments(APIView):
    # def get(self, request, videoId, format=None):
    #     comments = Comment.objects.filter(video_id=videoId)
    #     serializer = CommentSerializer(comments, many=True)
    #     return Response(serializer.data)
    def get(self, request, videoId, format=None):
        numPerPage = settings.PAGE_NUM
        comments = Comment.objects.filter(video_id=videoId)
        paginator = Paginator(comments, numPerPage)
        page = request.QUERY_PARAMS.get('page')
        try:
            comments = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            comments = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999),
            # deliver last page of results.
            comments = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = PaginatedCommentSerializer(comments,
                                         context=serializer_context)

        return Response(serializer.data)


    def post(self, request, videoId, format=None):
        try:
            placeVideo = PlaceVideo.objects.get(pk=videoId)
        except Place.DoesNotExist:
            raise Http404

        serializer = CommentSerializer(data=request.DATA)
        if serializer.is_valid():
            #serializer.object.type = 2 #1:like 2:comment
            serializer.object.creator = self.request.user
            serializer.object.video = placeVideo
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Authentication(APIView):
    def post(self, request, format=None):
        data = request.DATA
        facebookId = long(data["facebookId"])
        facebookAccessToken = str(data["accessToken"])

        # call facebook graph api to verify token
        graphURL =str.format('https://graph.facebook.com/v2.2/%s?access_token=%s' %(facebookId, facebookAccessToken))
        response = urlopen(graphURL).read()
        userInfo =json.loads(response)
        email = userInfo.get('email', '')
        firstName = userInfo.get('first_name', '')
        lastName = userInfo.get('last_name', '')
        name = userInfo.get('name', '')
        profileImage =str.format('//graph.facebook.com/%s/picture?type=large' % (facebookId))

        try:
            vsUser = VSUser.objects.get(thirdPartId=facebookId)
        except VSUser.DoesNotExist:
            # Create a new user. Note that we can set password
            # to anything, because it won't be checked; the password
            # from settings.py will.
            vsUser = VSUser(username=facebookId, thirdPartId=facebookId, thirdPartAccessToken=facebookAccessToken,
                            email=email,name= name, firstName=firstName, lastName=lastName, profileImage=profileImage)
            vsUser.save()

        token, created = Token.objects.get_or_create(user=vsUser)
        #refresh token if exist
        if not created:
            token.delete()
            token = Token.objects.create(user=vsUser)
            token.save()
        vsUser.accessToken = token.key
        vsUser.save()
        serializer = VSUserSerializer(vsUser)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UserDetail(APIView):
    def get(self, request, pk, format=None):
        try:
            vsUser = VSUser.objects.get(pk=pk)
        except PlaceVideo.DoesNotExist:
            raise Http404
        serializer = VSUserVideoSerializer(vsUser)
        return Response(serializer.data)


