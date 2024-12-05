from . import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class StudentForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields=['name', 'age', 'address']
        name = forms.CharField(label="Name", required=True)
        age = forms.IntegerField(label="Age", required=True, initial=0,widget=forms.NumberInput())
        address = forms.ModelChoiceField(
            label="Address",
            queryset=models.Address.objects.all().order_by("city"),
            widget=forms.ChoiceField()
        )

class StudentFormMany(forms.ModelForm):
    class Meta:
        model = models.Student2
        fields = ['name', 'age', 'address']
    name = forms.CharField(label="Name", required=True)
    age = forms.IntegerField(label="Age", required=True, initial=20, min_value=15, widget=forms.NumberInput())
    address = forms.ModelMultipleChoiceField(
        label="Address",
        queryset=models.Address2.objects.all().order_by("city"),
        widget=forms.CheckboxSelectMultiple()
    )

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']