from dataclasses import field
from rest_framework import serializers
from core.models import *


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)

    class Meta:
        model = Movie
        fields = ('name', 'description')


class CommentSerializerAdmin(serializers.HyperlinkedModelSerializer):
    approved = serializers.BooleanField(label='approved', required=True)

    class Meta:
        model = Comment
        fields = ('approved',)


class VoteSerializer(serializers.HyperlinkedModelSerializer):
    movie_id = serializers.IntegerField(required=True)
    vote = serializers.IntegerField(required=True)

    class Meta:
        model = Vote
        fields = ('movie_id', 'vote')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    movie_id = serializers.IntegerField(required=True)
    comment_body = serializers.CharField(required=True)

    class Meta:
        model = Vote
        fields = ('movie_id', 'comment_body')


class GetCommentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class GetMovieSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'name', 'description', 'rating')


class MovieIDSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(required=True)

    class Meta:
        model = Movie
        fields = ('id', 'name', 'description', 'rating')
