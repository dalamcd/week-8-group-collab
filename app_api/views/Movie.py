from django.http import HttpResponseServerError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from app_api.models.Movie import Movie

class MovieView(ViewSet):

    def list(self, request):
        movies = Movie.objects.all()
        user = request.auth.user
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

        
    def create(self,request):
        pass
        # foreign keys
        # user = request.auth.user
        # genre = Genre.objects.get(pk=request.data['genre'])
        # serializer = CreateMovieSerializer

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
            'id', 'title', 'description', 'run_time', 'date_released', 'genre'
        )
        depth = 1    
