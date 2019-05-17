import uuid

from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models


class BaseModel(models.Model):
    """
    Basic model to inherit.
    """
    uuid = models.UUIDField(_('UUID'), primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(_('Creado en'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Actualizado en'), auto_now=True)

    class Meta:
        abstract = True
        get_latest_by = 'created_at'
        ordering = ('-created_at',)

    def __str__(self):
        return '%s:%s' % (self.__class__.__name__.lower(), str(self.uuid)[:6])


class Person(BaseModel, AbstractUser):
    """
    Person model.
    """
    class Meta(BaseModel.Meta):
        verbose_name = _('Person')
        verbose_name_plural = _('People')

    def __str__(self):
        return self.username
