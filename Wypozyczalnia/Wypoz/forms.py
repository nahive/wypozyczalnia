from django import forms
from django.contrib.auth.models import User  #tutaj dac klient i firma jakos
from django.contrib.auth.forms import UserCreationForm
from Wypoz.models import Klient

class ClientRegistrationForm(UserCreationForm):
    imie = forms.TextInput()
    naz = forms.TextInput()
    miasto = forms.TextInput()
    ulica = forms.TextInput()
    tel = forms.NumberInput()
    email = forms.EmailField(required=True)
    num_dow = forms.NumberInput()

    class Meta:
        model = Klient
        fields = ('username','imie','naz','miasto','ulica','tel', 'email', 'password1', 'password2', 'num_dow')

    def save(self, commit=True):
        user = super(ClientRegistrationForm, self).save(commit=False)
        user.imie = self.cleaned_data['imie']
        user.naz = self.cleanded_data['naz']
        user.miast = self.cleaned_data['miasto']
        user.ulica = self.cleaned_data['ulica']
        user.tel = self.cleaned_data['tel']
        user.email = self.cleaned_data['email']
        user.num_dow = self.cleaned_data['num_dow']

        if commit:
            user.save()

        return user

    # tutaj jest form klienta, niby dziala, narazie brzydko, ale jakos nie dodaje do bazy tego klienta.