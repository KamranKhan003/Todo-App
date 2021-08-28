from  django import forms
from django.contrib.auth import get_user_model
from django.forms import fields, widgets
from django.forms.forms import Form
from .models import Todo

User = get_user_model()


# User Update Form
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','image']
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'UserName'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
        }


# Add Item
class AddTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title','description')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','autocomplete':'off','placeholder':'Title'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'autocomplete':'off','placeholder':'Description'}),
        }


class UpdateTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title','description','is_complete')
        labels = {
            'is_complete': 'Complete'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','autocomplete':'off','placeholder':'Title'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'autocomplete':'off','placeholder':'Description'}),
            'is_complete': forms.RadioSelect(attrs={'class':'form-check-input'}),
        }

class SearchForm(forms.Form):
    search = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control me-2','placeholder':'Search', 'autocomplete':'off'}))