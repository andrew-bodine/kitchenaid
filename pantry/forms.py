from django import forms
from models import *

class PantryItemForm( forms.ModelForm ):

	class Meta:
		model = PantryItem
		exclude = [ 'django_user' ]
