from django.db import models
from django.utils.translation import gettext as _


class Application(models.Model):

    STATUS_NEW = 'new'
    STATUS_SENT = 'sent'
    STATUS_RECEIVED = 'received'
    STATUS_ACCEPTED = 'accepted'
    STATUS_REFUSED = 'refused'
    STATUS_COMPLETED = 'completed'

    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=32, choices=(
        (STATUS_NEW, _('Новая')),
        (STATUS_SENT, _('Отправлена')),
        (STATUS_RECEIVED, _('Получена')),
        (STATUS_ACCEPTED, _('Одобрено')),
        (STATUS_REFUSED, _('Отказано')),
        (STATUS_COMPLETED, _('Выдано')),
    ))
