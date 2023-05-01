from django.db import models

# Create your models here.


class Answer(models.Model):  # 建立Answer資料庫存每題答案
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title


class Question(models.Model):  # 建立Question資料庫存每題題目
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title
