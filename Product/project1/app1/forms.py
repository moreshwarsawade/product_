from django import forms
from django.forms import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        models = Product
        fields = '__all__'


    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'discription': forms.TextInput(attrs={'class': 'form-control'}),
        'price': forms.IntegerInput(attrs={'class': 'form-control'}, render_value=True),
    }

    