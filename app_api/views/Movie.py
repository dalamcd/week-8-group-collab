from django.http import HttpResponseServerError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from app_api.models.Movie import Movie
from app_api.models.Genre import Genre
from django.contrib.auth.models import User


class MovieView(ViewSet):

    def list(self, request):
        movies = Movie.objects.all()
        user = request.auth.user
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

        # Let's burn this mother to the ground.
    def create(self,request):
        # Access foreign keys
        # Properties on data sent for POST:
            # 
        user = User.objects.get(pk=request.data['user'])
        genre = Genre.objects.get(pk=request.data['genre'])
        serializer = CreateMovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user, genre=genre)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def update(self, request, pk):
        pass

    def destroy(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = (
            'id', 'title', 'description', 'run_time', 'date_released', 'genre', 'user'
        )
        depth = 1    

class CreateMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = (
            'title',
            'description',
            'run_time',
            'date_released'
        )

        # Create movies with a user attached that isn't the user making the request. 
        # Think "suggested movies" on a streaming platform