from django.forms import Form, CharField, TextInput, PasswordInput


class LoginForm(Form):
    username = CharField(label='Username', widget=TextInput(attrs={
        'id': 'username'
    }))
    password = CharField(label='Password', widget=PasswordInput(attrs={
        'id': 'password'
    }))
