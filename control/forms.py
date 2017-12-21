from django import forms
from .models import *


class CheckoutContactForm(forms.Form):
    name = forms.CharField(required=True)
    password = forms.CharField(required=True)