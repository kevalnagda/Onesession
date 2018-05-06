from django import forms
from .models import UserDetails, FormDetails, ChangeUserDetails


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserDetails
        fields = ['sap', 'username', 'password', 'address']


class ConForm(forms.ModelForm):

    class Meta:
        model = FormDetails
        fields = ['sap', 'dept', 'date_of_birth', 'gender', 'year', 'train_class', 'station']


class ChangeForm(forms.ModelForm):

    class Meta:
        model = ChangeUserDetails
        fields = ['sap', 'dept', 'year', 'address', 'station', 'address_proof']

