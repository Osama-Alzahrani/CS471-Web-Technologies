from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta: 
        model = Book # tell form that model to map

        fields = '__all__' # tell form what to map from model
    title = forms.CharField(
        max_length=100,
        required=True,
        label="Title",
        widget= forms.TextInput( attrs= {
        'placeholder':'Enter title',
        })
    ) 
    price = forms.DecimalField(
        required=True,
        label="Price",
        initial=0.0,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            'step': '0.5',  # Enforces step increment of 0.5
            'type': 'number'  # Ensures the input type is number
        })

    ) 
    edition = forms.IntegerField(
        required=True,
        label="Edition",
        initial=1,
        widget=forms.NumberInput()
    )
    author = forms.CharField(
        max_length=100,
        required=True,
        label="Author",
        widget= forms.TextInput( attrs= {
        'placeholder':'Enter title',
        })

    ) 

    coverPage = forms.FileField(
        required=True,
        label="Cover Page",
        widget=forms.ClearableFileInput()
    )