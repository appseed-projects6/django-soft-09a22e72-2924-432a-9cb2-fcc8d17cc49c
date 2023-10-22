# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Undefined(models.Model):

    #__Undefined_FIELDS__

    #__Undefined_FIELDS__END

    class Meta:
        verbose_name        = _("Undefined")
        verbose_name_plural = _("Undefined")


class Book(models.Model):

    #__Book_FIELDS__
    title = models.CharField(max_length=255, null=True, blank=True)
    author = models.CharField(max_length=255, null=True, blank=True)

    #__Book_FIELDS__END

    class Meta:
        verbose_name        = _("Book")
        verbose_name_plural = _("Book")


class Transaction(models.Model):

    #__Transaction_FIELDS__
    book = models.CharField(max_length=255, null=True, blank=True)
    user = models.CharField(max_length=255, null=True, blank=True)

    #__Transaction_FIELDS__END

    class Meta:
        verbose_name        = _("Transaction")
        verbose_name_plural = _("Transaction")



#__MODELS__END
