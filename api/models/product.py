from django.db import models
from django.utils.translation import gettext as _


class Product(models.Model):

    TYPE_CREDIT_MORTGAGE = 'credit_mortgage'
    TYPE_CREDIT_CONSUMER = _('credit_consumer')
    TYPE_CREDIT_CAR = _('credit_car')

    agent = models.ForeignKey('Agent', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    rotation_start_at = models.DateTimeField()
    rotation_stop_at = models.DateTimeField()
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=32, choices=(
        (TYPE_CREDIT_MORTGAGE, _('Ипотека')),
        (TYPE_CREDIT_CONSUMER, _('Потребительский кредит')),
        (TYPE_CREDIT_CAR, _('Автокредит')),
    ))
    min_score = models.IntegerField()
    max_score = models.IntegerField()
