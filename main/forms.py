from django import forms
from multiupload.fields import MultiImageField


class ProductForm(forms.Form):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your product title'
    }))
    price = forms.FloatField(label='Price', widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))
    image = MultiImageField(min_num=1, max_num=10, max_file_size=1024*1024*5, required=True)
    description = forms.CharField(label='Description', widget=forms.Textarea(attrs={
        'class': 'form-control'
    }))
