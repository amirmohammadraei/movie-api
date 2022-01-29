import django_filters
from core.models import *

class CommentFilter(django_filters.FilterSet):
    movie_id = django_filters.NumberFilter(label='movie')
    # name = django_filters.CharFilter(field_name="name", required=False)
    class Meta:
        model = Comment
        fields = ('movie_id',)