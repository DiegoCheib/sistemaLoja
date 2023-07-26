from django import forms

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
        "nome": "sobrenome",
        "minlength": "3",
        "maxlength": "25",
        "display": "grid",
        "required": True}))



    
