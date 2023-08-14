from django.db import models

from account.models import CustomUser


class Artist(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    picture = models.URLField(blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name