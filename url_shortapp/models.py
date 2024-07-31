from django.db import models


class Links(models.Model):
    redirect_link = models.URLField()
    short_link = models.CharField(max_length=10, unique=True)

    def   str  (self) -> str:
        return self.short_link
