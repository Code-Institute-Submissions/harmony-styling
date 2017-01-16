from __future__ import unicode_literals
from django.shortcuts import render
from django.db import models
from django.conf import settings
from accounts import models as accounts_models

# Create your models here.


class ClothingItem(models.Model):
    image = models.ImageField(upload_to="images", blank=True, null=True)
    name = models.CharField(max_length=254, default='')
    # tag = models.CharField(max_length=30, blank=True, null=True)
    owner = models.ForeignKey('accounts.User', related_name='itemsOfClothing')
    def __str__(self):
        return self.name

class Outfit(models.Model):
    owner = models.ForeignKey('accounts.User', related_name='outfits')
    name = models.CharField(max_length=254, default='')
    description = models.CharField(max_length=254, default='')
    items = models.ManyToManyField(ClothingItem)
    image = models.ImageField(upload_to="images", blank=True, null=True)

    def __str__(self):
        return self.name




    def __unicode__(self):
        return self.name






