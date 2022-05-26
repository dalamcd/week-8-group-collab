from django.http import HttpResponseServerError
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from app_api.models import Movie
from app_api.models import Genre
from django.contrib.auth.models import User
from django.forms.models import model_to_dict

from rest_framework import serializers, status
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
        genre = Genre.objects.get(pk=request.data['genre'])
        user = User.objects.get(pk=request.data['user'])
        movie = Movie.objects.create(
            genre= genre,
            user = user,
            title = request.data['title'],
            description = request.data['description'],
            run_time = request.data['run_time'],
            date_released = request.data['date_released']
        )
        return Response(model_to_dict(movie), status=status.HTTP_201_CREATED)
    def update(self, request, pk):
        pass

    def destroy(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


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