from django import forms


class LoginForm(forms.Form):
    use_required_attribute = False

    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput)
