from django import forms


class RegisterForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(
        min_length=8, widget=forms.PasswordInput()
    )
    repeat_password = forms.CharField(
        min_length=8, widget=forms.PasswordInput()
    )
    are_you_older_18 = forms.BooleanField(required=False)


class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(
        min_length=8, widget=forms.PasswordInput()
    )



