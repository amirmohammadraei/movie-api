from rest_framework import generics, status
from .serializers import *
from core.models import *
from core.api.filter import *
from rest_framework.response import Response
from core.api.authentication import *
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


response_204 = Response({'status': 204, 'description': 'OK'}, status=status.HTTP_204_NO_CONTENT)
response_400 = Response({'status': 400, 'description': 'Bad request.'}, status=status.HTTP_400_BAD_REQUEST)
response_500 = Response({'status': 500, 'description': 'There is an internal issue.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
response_200 = Response({'status': 200, 'description': 'OK.'}, status=status.HTTP_200_OK)


class InsertMovie(generics.CreateAPIView):
    permission_classes = (AdminPermission,)
    serializer_class = MovieSerializer

    def post(self, request, *args, **kwargs):
        if set(request.data.keys()) == set(['name', 'description']):
            try:
                Movie.objects.create(name=request.data['name'], description=request.data['description'])
                return response_204
            except: return response_500
        else: return response_400

class ManageMovie(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    permission_classes = (AdminPermission,)

    def put(self, request, *args, **kwargs):
        if set(request.data.keys()) == set(['name', 'description']):
            try:
                Movie.objects.get(id=kwargs['pk'])
                Movie.objects.filter(id=kwargs['pk']).update(name=request.data['name'], description=request.data['description'])
                return response_204
            except:  return response_400
        else: return response_400

    def delete(self, request, *args, **kwargs):
        try:
                movie = Movie.objects.get(id=kwargs['pk'])
                movie.delete()
                return response_204
        except:  return response_400


class ManageComment(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializerAdmin    

    def put(self, request, *args, **kwargs):
        if set(request.data.keys()) == set(['approved']):
            try:
                Comment.objects.get(id=kwargs['pk'])
                Comment.objects.filter(id=kwargs['pk']).update(approved=request.data['approved'])
                return response_204
            except:  return response_400
        else: return response_400

    def delete(self, request, *args, **kwargs):
        try:
                comment = Comment.objects.get(id=kwargs['pk'])
                comment.delete()
                return response_204
        except:  return response_400


class UserVote(generics.CreateAPIView):
    serializer_class = VoteSerializer
    permission_classes = (UserPermission,)

    def post(self, request, *args, **kwargs):
        if set(request.data.keys()) == set(['movie_id', 'vote']):
            try:
                Vote.objects.create(rating=request.data['vote'], movie_id=request.data['movie_id'], user=request.user)
                return response_204
            except: return response_500
        else: return response_400


class UserComment(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = (UserPermission,)

    def post(self, request, *args, **kwargs):
        if set(request.data.keys()) == set(['movie_id', 'comment_body']):
            try:
                Movie.objects.get(id=request.data['movie_id'])
                Comment.objects.create(comment=request.data['comment_body'], movie_id=request.data['movie_id'], user=request.user)
                return response_200
            except: return response_400
        else: return response_400


class CommentAPI(generics.ListAPIView):
    permission_classes = (AnonymousPermission,)
    filter_backends = [DjangoFilterBackend]
    filter_class = CommentFilter
    serializer_class = GetCommentSerializer

    def get(self, request, *args, **kwargs):
        try:
            mv = Movie.objects.filter(id=request.query_params['movie_id'])
            mv[0]
        except:
            return response_400
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        try:
            return Comment.objects.filter(movie_id=self.request.query_params['movie_id'])
        except:
            return Comment.objects.none()


class MovieAPI(generics.ListAPIView):
    permission_classes = (AnonymousPermission,)
    serializer_class = GetMovieSerializer

    def get_queryset(self):
        return Movie.objects.all().order_by('id')


class MovieWithIDAPI(generics.ListAPIView):
    permission_classes = (AnonymousPermission,)
    serializer_class = MovieIDSerializer

    def get(self, request, *args, **kwargs):
        try:
            Movie.objects.get(id=kwargs['pk'])
        except:
            return response_400
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return Movie.objects.filter(id=self.kwargs['pk'])