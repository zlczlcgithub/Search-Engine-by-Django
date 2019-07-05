from django.conf import settings
from django.db import models
from django.utils import timezone


class Sentence(models.Model):
    sentence = models.CharField(max_length=200)
    super_cat = models.CharField(max_length=200, default = "")
    sub_cat = models.CharField(max_length=200, default = "")
