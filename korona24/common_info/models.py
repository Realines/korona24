from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models.singleton_model import SingletonModel


class SiteSettings(SingletonModel):
    
