from django import forms
from django.forms.widgets import CheckboxInput

class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username", 
        error_messages={
            "required":"Username in required",},
            )
    password = forms.CharField(
        label="Password", 
        error_messages={
            "required":"Password in required",},
        widget=forms.PasswordInput
        )
    remember = forms.BooleanField(
        widget=CheckboxInput,
        label="Remember Me",
        required=False
        )
    
class RegForm(forms.Form):
    firstname = forms.CharField(
        max_length=10,
        min_length=3,
        label="Firstname", 
        error_messages={
            "required":"Firstname in required",
            "max_length":"Put shorter name",
            "min_length":"Put longer name"},
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'First Name'})
        )
    lastname = forms.CharField(
        max_length=10,
        min_length=3,
        label="Lastname", 
        error_messages={
            "required":"Lastname in required",
            "max_length":"Put shorter name",
            "min_length":"Put longer name"},
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Last Name'})
        )
    username = forms.CharField(
        max_length=50,
        min_length=8,
        label="Username", 
        error_messages={
            "required":"Username in required",
            "max_length":"Put shorter name",
            "min_length":"Put longer name"},
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'User Name'})
        )
    email = forms.EmailField(
        max_length=40,
        min_length=15,
        label="E-mail",
        error_messages={
            "required":"Email is required",
            "max_length":"Put shorter email",
            "min_length":"Put longer email"},
        widget=forms.EmailInput(attrs={
                'class':'form-control',
                'placeholder':'Email'})
        )
    password = forms.CharField(
        max_length=16,
        min_length=8,
        label="Password", 
        error_messages={
            "required":"Password in required",
            "max_length":"Put shorter password",
            "min_length":"Put longer password"},
        widget=forms.PasswordInput(attrs={
                'class':'form-control',
                'placeholder':'Password'})
        )
    repassword = forms.CharField(
        max_length=16,
        min_length=8,
        error_messages={
            "required":"Password in required",
            "max_length":"Put shorter password",
            "min_length":"Put longer password"},
        widget=forms.PasswordInput(attrs={
                'class':'form-control',
                'placeholder':'RePassword'})
        )
        
    