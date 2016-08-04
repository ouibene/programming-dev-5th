import re
from django.db import models
from django.forms import ValidationError
from django.utils import timezone


def lnglat_validator(value):
    if not re.match(r'^(\d+\.?\d*),(\d+\.?\d*)$', value):
        raise forms.ValidationError("Invalid Lanlat Type")


class Person(models.Model) :
    name = models.CharField(max_length = 20, default='Jiwoo')
    level = models.IntegerField(default=1)

    def __str__(self) :
        return self.name


class Pokemon(models.Model) :
    name = models.CharField(max_length = 20)
    level = models.IntegerField(default=1)
    #attack =
    #defense =
    #moves =
    captured_date = models.DateTimeField(default = timezone.now)
    place = models.ForeignKey("Place")
    person = models.ForeignKey("Person")

    def __str__(self) :
        return self.name


class Place(models.Model) :
    name = models.CharField(max_length = 20)
    lnglat = models.CharField(max_length=50,
        validators = [lnglat_validator], help_text='위도,경도 포맷으로 입력')

    def __str__(self) :
        return self.name
