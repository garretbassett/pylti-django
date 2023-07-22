from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    # Additional fields for the user model
    # e.g., profile picture, bio, etc.
    bio = models.TextField(blank=True)
    groups = models.ManyToManyField(Group, related_name='user_set_game', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='user_set_game', blank=True)


class Quiz(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    # Other fields for the quiz model
    # e.g., time_limit, instructions, etc.


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=255)
    # Other fields for the question model
    # ...


class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    chosen_answer = models.CharField(max_length=255)
    # Other fields for the answer model
    # ...


class Score(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    # Other fields for the score model
    # ...