from django.db import models
from model_utils.models import TimeStampedModel


class State(TimeStampedModel):
    name = models.CharField(max_length=30)
    slug = models.CharField(max_length=2)
    code = models.CharField(max_length=2)

    def __str__(self):
        return "{} - {}".format(self.name, self.slug)


class City(TimeStampedModel):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=6)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.name, self.code)
