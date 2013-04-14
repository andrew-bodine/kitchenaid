from django import forms
from models import *

class PantryItemForm( forms.ModelForm ):

	class Meta:
		model = PantryItem
		exclude = [ 'django_user' ]
		widgets = {
				'name': forms.TextInput( attrs={ 'placeholder': 'Item Name', 'class': 'span3' } ),
				'amount': forms.TextInput( attrs={ 'placeholder': 'Quantity', 'class': 'span2' } ),
				'unit': forms.Select( attrs={ 'class': 'span2' } ),
		}
