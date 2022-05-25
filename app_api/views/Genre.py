from django.http import HttpResponseServerError
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import serializers, status
from app_api.models.Genre import Genre
from rest_framework import serializers

class GenreView(ViewSet):
    """View for Genres"""

    def list(self, request):
        """"Handle get request for Genres"""
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)

    def create(self, request):
        pass

    def update(self, request, pk):
        pass

    def destroy(self, request, pk):
        pass

class GenreSerializer(serializers.ModelSerializer):
    """JSON serializerserializers"""
    class Meta:
     
        model = Genre
        Fields =Genre
