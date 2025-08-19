from django import forms
from .models import ShippingAddress
class ShippingForm(forms.ModelForm):
    Shipping_full_name=forms.CharField(label="",widget=forms.TextInput({'class':'form-control','placeholder':'Full Name'}),required=True)
    Shipping_email=forms.CharField(label="",widget=forms.TextInput({'class':'form-control','placeholder':'Email Adress'}),required=True)
    Shipping_address1=forms.CharField(label="",widget=forms.TextInput({'class':'form-control','placeholder':'Address1'}),required=True)
    Shipping_address2=forms.CharField(label="",widget=forms.TextInput({'class':'form-control','placeholder':'Address2'}),required=False)
    Shipping_city=forms.CharField(label="",widget=forms.TextInput({'class':'form-control','placeholder':'City'}),required=True)
    Shipping_state=forms.CharField(label="",widget=forms.TextInput({'class':'form-control','placeholder':'State'}),required=False)
    Shipping_zipcode=forms.CharField(label="",widget=forms.TextInput({'class':'form-control','placeholder':'Zipcode'}),required=False)
    Shipping_country=forms.CharField(label="",widget=forms.TextInput({'class':'form-control','placeholder':'Country'}),required=True)
    
    class Meta:
        model:ShippingAddress
        fields='__all__'

        exclude=['user',]



    # shipping_user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    
