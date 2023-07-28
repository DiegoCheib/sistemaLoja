from django import forms
from .models import userTest
#define your forms here

class inputName(forms.Form):
    nome = forms.CharField(label='', help_text='',widget=forms.TextInput(attrs={
        "class": "input__field",
        "name": "nome",
        "minlength": "3",
        "maxlength": "25",
        "display": "grid",
        "required": True}))

class inputSobrenome(forms.Form):
    sobrenome = forms.CharField(label='', help_text='',widget=forms.TextInput(attrs={
        "class": "input__field",
        "name": "sobrenome",
        "minlength": "3",
        "maxlength": "25",
        "display": "grid",
        "required": True}))
    

class inputEmail(forms.Form):
    email = forms.CharField(label='', help_text='',widget=forms.EmailInput(attrs={
        "class": "input__field",
        "name": "email",
        "type": "email",
        "maxlength": "100",
        "display": "grid",
        "Required": True
    }))
    def clean(self):
        email = self.cleaned_data.get('email')
        if userTest.objects.filter(useremail=email).exists():
            raise forms.ValidationError("Uma conta com este email ja existe")
        else:
            pass
class inputPassowrd(forms.Form):
    password = forms.CharField(label='', help_text='',widget=forms.PasswordInput(attrs={
        "class": "input__field",
        "name": "password",
        "type": "password",
        "minlength": "3",
        "maxlength": "50",
        "display": "grid",
        "Required": True
    }))

class inputPhone(forms.Form):
    telefone = forms.CharField(label='', help_text='', widget=forms.TextInput(attrs={
        "class": "input__field",
        "name": "telefone",
        "type": "tel",
        "pattern": "\d{2,3}\s?\d{9}",
        "minlength": "11",
        "display": "grid",
        "Required": True
    }))

class inputCpf(forms.Form):
    cpf = forms.CharField(label='', help_text='',widget=forms.TextInput(attrs={
        "class": "input__field",
        "name": "cpf",
        "type": "text",
        "pattern": "\d{3}.?\d{3}.?\d{3}-?\d{2}",
        "minlength": "11",
        "display": "grid",
        "Required": True
    }))
