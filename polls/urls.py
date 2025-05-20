from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PollViewSet, FavoriteViewSet


router = DefaultRouter()
router.register(r'polls', PollViewSet, basename='poll')
router.register(r'favorites', FavoriteViewSet, basename='favorite')


urlpatterns = [    
    path('', include(router.urls)),
]