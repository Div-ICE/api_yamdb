from django.db import router
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    ReviewViewSet, TitleViewSet, UsersViewSet)

router = DefaultRouter()

router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'comments', CommentViewSet, basename='comments')
router.register(r'genres', GenreViewSet, basename='genres')
router.register(r'reviews', ReviewViewSet, basename='reviews')
router.register(r'titles', TitleViewSet, basename='titles')
router.register(r'users', UsersViewSet, basename='users')
router.register(
    r'title/(?P<title_id>[\d]+)/reviews',
    ReviewViewSet, basename='reviews'
)
"""Роуты надо править, есть неправильные и много не хватает"""


urlpatterns = [
    path('v1/', include(router.urls)),
]
