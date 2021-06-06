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
    chapter = models.Foreignkey(Chapter)
