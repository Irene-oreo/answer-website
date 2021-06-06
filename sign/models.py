from django.db import models

# Create your models here.


class lists(models.Model):
    title = models.CharField(max_length=5, unique=True)
    content = models.TextField(max_length=20)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Chapter(models.Model):
    title = models.CharField(max_length=5)

    def __str__(self):
        return self.title


class Answer(models.Model):
    #chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title
