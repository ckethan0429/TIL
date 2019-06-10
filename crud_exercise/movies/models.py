from django.db import models


# Create your models here.
class Movie(models.Model):
    title = models.TextField()
    title_en = models.TextField()
    audience = models.IntegerField()
    open_date = models.DateTimeField(auto_now_add=True)
    genre = models.TextField()
    watch_grade = models.TextField()
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f'{self.id}글 : {self.title}'


