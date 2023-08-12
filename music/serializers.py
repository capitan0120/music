from rest_framework import serializers
from music.models import Song, Artist, Album
from drf_writable_nested import WritableNestedModelSerializer
from rest_framework.exceptions import ValidationError

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()
    class Meta:
        model = Album
        fields = ['id', 'title', 'artist', 'cover']


class SongSerializer(serializers.ModelSerializer):
    album = AlbumSerializer()
    class Meta:
        model = Song
        fields = ('id', 'title', 'listened', 'cover', 'source', 'album')

    # def validate_source(self, value):
    #     if not value.endswith('.mp3'):
    #         raise ValidationError(detail="mp3 bo'lishi kerak")
    #     return value