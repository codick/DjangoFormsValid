from django import forms

class Registration(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "registration_input", "placeholder": "Логин"}), required=True, label='Введите имя')
    email = forms.EmailField(widget=forms.TextInput(attrs={"class": "registration_input", "placeholder": "Почта"}), required=True, label='Введите почту')
    password = forms.CharField(widget=forms.TextInput(attrs={"class": "registration_input", "placeholder": "Пароль"}), required=True, label='Введите пароль')

class SignForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "registration_input", "placeholder": "Логин"}), required=True, label='Введите имя')
    password = forms.CharField(widget=forms.TextInput(attrs={"class": "registration_input", "placeholder": "Пароль"}), required=True, label='Введите пароль')