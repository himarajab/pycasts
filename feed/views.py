from .models import Feed
from pprint import pprint
from rest_framework import generics, permissions,status
from feed.serializers import FeedSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import serializers

class FeedListView(generics.ListAPIView):
    """
    List all Feed
    """
    serializer_class = FeedSerializer
    def get_queryset(self):
        queryset = Feed.objects.all()
        return queryset
    

class Subscribe(APIView):
    permission_classes = (
		permissions.IsAuthenticated,
	)
    def post(self, request,feed_id):
        user_id = request.user.id
        serializer = FeedSerializer(data=request.data)
        feed = Feed.objects.get(id = feed_id)
        updated=feed.user.add(user_id)  
        return Response({"status": "success"}, status=status.HTTP_200_OK)


class Unsubscribe(APIView):
    permission_classes = (
		permissions.IsAuthenticated,
	)
    def post(self, request,feed_id):
        user_id = request.user.id
        serializer = FeedSerializer(data=request.data)
        feed = Feed.objects.get(id = feed_id)
        updated=feed.user.remove(user_id)
        return Response({"status": "success"}, status=status.HTTP_200_OK)
    