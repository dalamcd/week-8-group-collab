from django.http import HttpResponseServerError
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from app_api.models import Movie
from app_api.models import Genre
from rest_framework import serializers

class MovieView(ViewSet):

    def list(self, request):
        movies = Movie.objects.all()
        genre = self.request.query_params.get('genre', None)
        if genre is not None:
            movies = movies.filter(genre=genre)
            for movie in movies:
                genre = Genre.objects.get(pk=movie.genre.id)
                movie.genre_name = genre.name
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    def create(self, request):
        pass

    def update(self, request, pk):
        pass

    def destroy(self, request, pk):
        pass


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('id', 'name')
    
class MovieSerializer(serializers.ModelSerializer):
        genre_name = serializers.CharField()

        class Meta:
            model = Movie
            fields = ('id', 'title', 'description', 'run_time', 'user', 'date_released', 'genre', 'genre_name')
            # depth = 1