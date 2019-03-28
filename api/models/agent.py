from django.db import models


class Agent(models.Model):

    title = models.CharField(max_length=255)
