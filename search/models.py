from django.conf import settings
from django.db import models
from django.utils import timezone


class Sentence(models.Model):
    text = models.CharField(max_length=200)  
