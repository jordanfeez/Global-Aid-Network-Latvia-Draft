from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Address
from .models import GenderChoice
from.countries_list import COUNTRY_CHOICES

User = get_user_model()

class CustomSignUpForm(UserCreationForm):
    first_name = forms.CharField(
         max_length=30,
          required=True,
          label='First Name',
          help_text="Enter your first name.",
          widget=forms.TextInput(attrs={'class':'first_name'})
          )
    
    last_name = forms.CharField(
         max_length=30,
           required=True,
           label="Last Name",
           help_text="Enter your last name.",
           widget=forms.TextInput(attrs={'class':'last_name'})
           )
    

    class Meta:
        fields = ('username', 'first_name', 'last_name', 'email', 'password1',  'password2')
        model = User
        labels ={
            'username': 'Username', 
        }
        help_texts  = {
            'username' : " ",
            'password1': "",
            'password2': " ",
        }

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Username'

class GenderSelect(forms.ModelForm):
    class Meta:
        model= GenderChoice
        fields= ['gender']
        widgets = {'gender': forms.RadioSelect(attrs={'class': 'gender-buttons'}),}

class HomeAddress(forms.ModelForm):
    address_one = forms.CharField(
        required = True,
        max_length = 100,
        label = "Address 1",
        widget= forms.TextInput(attrs={'class':'address1'})
    )

    address_two = forms.CharField(
        required = False,
        max_length = 100,
        label = "Address line 2",
        widget= forms.TextInput(attrs={'class':'address2'})
    )

    city = forms.CharField(
        required = True,
        max_length = 100,
        label = "City",
        widget= forms.TextInput(attrs={'class':'city'})
    )
    
    zipcode = forms.CharField(
        required = True,
        max_length = 100,
        label = "Zipcode",
        widget= forms.TextInput(attrs={'class':'zipcode'})
      
    )

    country = forms.ChoiceField(
        required = True,
        label = "Country",
        choices= [(" ", '---Please Select a Country---')] + COUNTRY_CHOICES,
        widget= forms.Select(attrs={'class':'countries', 'data-placeholder':'<--Select a Country-->'})
    )

    class Meta:
        model = Address
        fields = ['address_one', 'address_two', 'city','zipcode', 'country']
     