from django import forms
from store.models import *
class ProjectUserLogInForm(forms.Form):
    email=forms.EmailField(max_length=50)
    password=forms.CharField(widget=forms.PasswordInput())
    # class Meta:
    #     model=projectUserModel
    #     fields=['email','password']
    #     widgets={
    #         'password':forms.PasswordInput()
    #     }
class ProjectUserSignUpModelForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=projectUserModel
        fields='__all__' 
        widgets={
            'password':forms.PasswordInput()
        }