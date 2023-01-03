from django.db import models

from wagtail.models import Page


class HomePage(Page):
    pass


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
