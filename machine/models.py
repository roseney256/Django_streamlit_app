from typing import Iterable, Optional
from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Data (models.Model):

    DATE = models.DateField(_("DATE"))
    MinTemp = models.FloatField(_("MinTemp"))
    MaxTemp = models.FloatField(_("MaxTemp"))
    AvgTemp = models.FloatField(_("AvgTemp"))
    Total = models.BigIntegerField(_("Total"))
    Local = models.BigIntegerField(_("Local"))
    Exotic = models.BigIntegerField(_("Exotic"))
    EF = models.FloatField(_("EF"))
    Agric = models.BigIntegerField(_("Agric"))

    