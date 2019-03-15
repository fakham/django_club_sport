# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

GENRE_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
)


class Adherent(User):
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    adresse = models.CharField(max_length=200)
    genre = models.CharField(max_length=1, choices=GENRE_CHOICES)
    tel = models.CharField(max_length=20)

    def __str__(self):
        return self.username


class Sport(models.Model):
    designation = models.CharField(max_length=100)
    tarif = models.DecimalField(decimal_places=2, max_digits=9)

    def __str__(self):
        return self.designation


class Inscription(models.Model):
    adherent = models.ForeignKey(Adherent, on_delete=models.CASCADE)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('adherent', 'sport'),)

    def __str__(self):
        return str(self.adherent) + ', ' + str(self.sport)
