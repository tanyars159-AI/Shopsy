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
class PaymentForm(forms.Form):
    card_name=forms.CharField(label="",widget=forms.TextInput({'class':'form-control','placeholder':'Name of card'}),required=True)
    card_number=forms.CharField(label="",widget=forms.TextInput({'class':'form-control','placeholder':'Card number'}),required=True)
    card_exp_date=forms.CharField(label="",widget=forms.TextInput({'class':'form-control','placeholder':'Card expiry date'}),required=True)
    card_cvv_number=forms.CharField(label="",widget=forms.TextInput({'class':'form-control','placeholder':'Cvv Number'}),required=True)
    card_address1=forms.CharField(label="",widget=forms.TextInput({'class':'form-control','placeholder':'Adress1'}),required=True)
    card_adress2=forms.CharField(label="",widget=forms.TextInput({'class':'form-control','placeholder':'Adress2'}),required=False)
    card_city=forms.CharField(label="",widget=forms.TextInput({'class':'form-control','placeholder':'City'}),required=True)
    card_state=forms.CharField(label="",widget=forms.TextInput({'class':'form-control','placeholder':'State'}),required=True)
    card_zipcode=forms.CharField(label="",widget=forms.TextInput({'class':'form-control','placeholder':'Zipcode'}),required=True)
    card_country=forms.CharField(label="",widget=forms.TextInput({'class':'form-control','placeholder':'Country'}),required=True)

    
    # shipping_user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    
