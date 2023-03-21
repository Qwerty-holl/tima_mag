from django import forms
from .models import *


class AddPostForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия Имя Отчество'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите ваш E-mail'}))
    number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите номер телефона'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Оставьте ваше сообщение'}))

    # fields = ['title', 'anons', 'full_text', 'date']
    # widgets = {
    #     'title': forms.TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Название статьи'
    #     }),
    #     'anons': forms.TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Анонс статьи'
    #     }),
    #     'date': forms.DateTimeInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Дата публикации'
    #     }),
    #     'full_text': forms.Textarea(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Текст статьи'
    #     }),
    #
    # }