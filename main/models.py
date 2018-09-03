from django.db import models


class UsefulNumber(models.Model):
    number = models.IntegerField()


class UsefulText(models.Model):
    text = models.TextField()
