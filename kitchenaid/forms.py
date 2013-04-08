from django import forms

class FoodieCredentialsForm( forms.Form ):
	email = forms.EmailField( widget=forms.TextInput( attrs={ 'placeholder': 'email', 'class': 'span3' } ) )
	password = forms.CharField( widget=forms.PasswordInput( attrs={ 'placeholder': 'password', 'class': 'span3' } ) )

class FoodieRegistrationForm( forms.Form ):
	first_name = forms.CharField( max_length=30, widget=forms.TextInput( attrs={ 'placeholder': 'first name', 'class': 'span3' } ) )
	last_name = forms.CharField( max_length=30, widget=forms.TextInput( attrs={ 'placeholder': 'last name', 'class': 'span3' } ) )
	email = forms.EmailField( widget=forms.TextInput( attrs={ 'placeholder': 'email', 'class': 'span6' } ) )
	password = forms.CharField( widget=forms.PasswordInput( attrs={ 'placeholder': 'password', 'class': 'span3' } ) )
	password_again = forms.CharField( widget=forms.PasswordInput( attrs={ 'placeholder': 'password again', 'class': 'span3' } ) )
