from django.db import models
from django.utils.translation import gettext as _

from django.contrib.postgres.fields import DateTimeRangeField


class Product(models.Model):

    class Type:
        MORTGAGE = _('Ипотека')
        CONSUMER = _('Потребительский кредит')
        CAR = _('Автокредит')

    agent = models.ForeignKey('Agent', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    rotation_period = DateTimeRangeField()
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=32, choices=Type.__dict__.items())
    min_score = models.IntegerField()
    max_score = models.IntegerField()
