from django.db import models
from account.models import CustomUser


class Album(models.Model):
    artist = models.ForeignKey("music.Artist", on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, null=False, blank=False)
    cover = models.URLField(blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title
