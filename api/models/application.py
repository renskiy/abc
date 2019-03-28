from django.db import models
from django.utils.translation import gettext as _


class Application(models.Model):

    class Status:
        NEW = _('Новая')
        SENT = _('Отправлена')
        RECEIVED = _('Получена')
        ACCEPTED = _('Одобрено')
        REFUSED = _('Отказано')
        COMPLETED = _('Выдано')

    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=32, choices=Status.__dict__.items())
