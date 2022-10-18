import datetime

from django.db import models
from django.utils import timezone

from django.contrib import admin

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text


class Genre(models.Model):
    genre = models.CharField(max_lenght=30)
    def __str__(self):
        return self.genre


class Movie(models.Model):
    title = models.CharField(max_lenght=50)
    author = models.ForeignKey(Author)
    genre = models.ForeignKey(Genre)
    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=50)
    works = models.ForeignKey([Movie])
