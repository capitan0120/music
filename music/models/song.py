from django.db import models

from account.models import CustomUser


class Song(models.Model):
    album = models.ForeignKey("music.Album", on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200, null=False, blank=False)
    cover = models.URLField(blank=True)
    source = models.URLField(blank=False, null=False)
    listened = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)


    def __str__(self):
        return self.title
