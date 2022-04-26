from django.db import router
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CategoryViewSet, CommentViewSet, CreateUserViewSet,
                    GenreViewSet, ReviewViewSet, TitleViewSet, UserViewSet,
                    token_post, users_me)

router = DefaultRouter()

router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'genres', GenreViewSet, basename='genres')
router.register(r'titles', TitleViewSet, basename='titles')
router.register(r'users', UserViewSet, basename='users')
router.register(
    r'titles/(?P<title_id>[\d]+)/reviews',
    ReviewViewSet, basename='reviews'
)
router.register(
    r'titles/(?P<title_id>[\d]+)/reviews/(?P<review_id>[\d]+)/comments',
    CommentViewSet, basename='comments'
)
"""Роуты надо править, есть неправильные и много не хватает"""


urlpatterns = [
    path('v1/users/me/', users_me),
    # path("v1/api-token-auth/", views.obtain_auth_token),
    path("v1/auth/signup/", CreateUserViewSet.as_view(), name='signup'),
    path("v1/auth/token/",
         token_post, name='token'),
    path('v1/', include(router.urls)),
]
