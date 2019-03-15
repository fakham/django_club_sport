# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Adherent, Sport, Inscription

# Register your models here.

admin.site.register(Adherent)
admin.site.register(Inscription)
admin.site.register(Sport)
