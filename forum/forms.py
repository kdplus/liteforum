from django import forms
from pagedown.widgets import AdminPagedownWidget

class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    #phone = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm', widget=forms.PasswordInput)

class PostForm(forms.Form):
    caption = forms.CharField(label='title', max_length=200)
    content = forms.CharField(widget=AdminPagedownWidget())

class TagForm(forms.Form):
    tag_name = forms.CharField()
