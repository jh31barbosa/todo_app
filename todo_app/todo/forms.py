from cProfile import label
from django import forms
from .models import Todo

class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields=('title','status')
        widgets= {
        'title':forms.TextInput(attrs={
                'class':'form-control'
            }),
        'status':forms.CheckboxInput(attrs={
                'class':'form-check-input'
            })
        }