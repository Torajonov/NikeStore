from django import forms
from .models import *
class AddOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['products','payed', 'total_sum']
