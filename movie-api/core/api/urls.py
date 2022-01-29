from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.api import views

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/movie/', views.InsertMovie.as_view()),
    path('admin/movie/<pk>', views.ManageMovie.as_view()),
    path('admin/comment/<pk>', views.ManageComment.as_view()), 
    path('user/vote/', views.UserVote.as_view()),
    path('user/comment/', views.UserComment.as_view()),
    path('comments/', views.CommentAPI.as_view()),
    path('movies/', views.MovieAPI.as_view()),
    path('movie/<pk>', views.MovieWithIDAPI.as_view()),
]