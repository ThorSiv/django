# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django import forms

class Host(forms.Form):
 	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'密码'}))
