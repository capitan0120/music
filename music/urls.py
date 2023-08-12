from django.db import router
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import SongViewSet, AlbumViewSet, ArtistViewSet

router = DefaultRouter()
router.register(r'songs', SongViewSet, basename='songs')
router.register(r'albums', AlbumViewSet, basename='albums')
router.register(r'artists', ArtistViewSet, basename='artists')
urlpatterns = router.urls
# urlpatterns = [
#     path('songs/', SongsAPIView.as_view(), name="songs")
# ]