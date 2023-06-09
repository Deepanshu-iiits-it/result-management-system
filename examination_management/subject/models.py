from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel
from django.core import validators

from examination_management.core.behaviours import StatusMixin


class Subject(StatusMixin, TimeStampedModel):
    code = models.CharField(_('Code'), max_length=100, primary_key=True)
    name = models.CharField(_('Name'), max_length=100, null=True, blank=True)
    credit = models.IntegerField(_('Credit'), null=True, blank=True, default=0,
                                 validators=[validators.MinValueValidator(0),])
    is_elective = models.BooleanField(_('Is Elective'), default=False)

    def __str__(self):
        return str(self.code)
