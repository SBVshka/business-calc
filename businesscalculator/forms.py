import datetime

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

year_now = datetime.date.today().year
from django import forms
from .models import *


class CompanyDataForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['year'].initial = year_now
        self.fields['country'].initial = 'РФ'

    class Meta:
        model = Company
        fields = ('name', 'year', 'founder', 'country', 'form', 'industry', 'activity', 'email', 'tel')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ромашка'}),
            'founder': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Иванова И.А.'}),
            'form': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ПАО'}),
            'industry': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Розничная торговля'}),
            'activity': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Продажа цветов'}),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'ivanova94@mail.ru'}),
            'tel': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+79247878787'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'class': 'form-control'})
        }

    def clean_year(self):
        year = self.cleaned_data['year']
        if year > year_now:
            print('error')
            raise ValidationError('Вы из будущего что ли?:)')
        return year


class BalanceDataForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['year'].initial = year_now
        self.fields['company'].empty_label = 'Выберите компанию'

    class Meta:
        model = Balance
        fields = '__all__'
        widgets = {
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                "cols": 60, "rows": 5}),
            'current_assets': forms.NumberInput(attrs={'class': 'form-control'}),
            'fixed_assets': forms.NumberInput(attrs={'class': 'form-control'}),
            'equity': forms.NumberInput(attrs={'class': 'form-control'}),
            'current_liabilities': forms.NumberInput(attrs={'class': 'form-control'}),
            'long_liabilities': forms.NumberInput(attrs={'class': 'form-control'}),
            'company': forms.Select(attrs={'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'class': 'form-control'})
        }

    def clean_year(self):
        year = self.cleaned_data['year']
        if year > year_now:
            print('error')
            raise ValidationError('Вы из будущего что ли?:)')
        return year


class StatementForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['year'].initial = year_now
        self.fields['company'].empty_label = 'Выберите компанию'

    class Meta:
        model = Statement
        fields = '__all__'
        widgets = {
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                "cols": 60, "rows": 5}),
            'returns': forms.NumberInput(attrs={'class': 'form-control'}),
            'oper_exp': forms.NumberInput(attrs={'class': 'form-control'}),
            'other_costs': forms.NumberInput(attrs={'class': 'form-control'}),
            'taxes': forms.NumberInput(attrs={'class': 'form-control'}),
            'revenue': forms.NumberInput(attrs={'class': 'form-control'}),
            'company': forms.Select(attrs={'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'class': 'form-control'})
        }

    def clean_year(self):
        year = self.cleaned_data['year']
        if year > year_now:
            print('error')
            raise ValidationError('Вы из будущего что ли?:)')
        return year


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['expert'].empty_label = 'Выберите свою фамилию'
        self.fields['company'].empty_label = 'Выберите компанию'

    class Meta:
        model = Report
        fields = '__all__'
        widgets = {
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                "cols": 60, "rows": 10}),
            'select': forms.RadioSelect(attrs={'class': 'form-check-inline'}),
            'company': forms.Select(attrs={'class': 'form-control'}),
            'expert': forms.Select(attrs={'class': 'form-control'})
        }


User = get_user_model()


class RegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ivan_ivanov'}),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Иван'}),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Иванов'}),
            'form': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ПАО'}),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'ivanova94@mail.ru'}),
            'password1': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Надёжный'}),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ещё раз надёжный'})
        }
