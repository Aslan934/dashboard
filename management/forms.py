from django import forms



class LoginForm(forms.Form):
    email = forms.CharField(label='Your email')
    password = forms.CharField(
        widget=forms.PasswordInput, label='Your password')