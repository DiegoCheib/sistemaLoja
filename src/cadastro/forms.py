from django import forms

#define your forms here

class inputName(forms.Form):
    nome = forms.CharField(label='', help_text='',widget=forms.TextInput(attrs={
        "class": "input__field",
        "name": "nome",
        "minlength": "3",
        "maxlength": "25",
        "required": True}))
    
