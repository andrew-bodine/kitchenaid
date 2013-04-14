from django import forms
from models import *

class RecipeForm( forms.ModelForm ):
	
	class Meta:
		model = Recipe
		exclude = [ 'django_user' ]
		widgets = {
			'name': forms.TextInput( attrs={ 'placeholder': 'Recipe Name', 'class': 'span4' } ),
			'preparation_time': forms.TextInput( attrs={ 'placeholder': 'Preparation Time', 'class': 'span2' } ),
			'difficulty': forms.Select( attrs={ 'class': 'span2' } ),
			'meal_time': forms.Select( attrs={ 'class': 'span2' } ),
			'directions': forms.Textarea( attrs={ 'placeholder': 'Recipe Instructions', 'class': 'span8' } ),
		}

class IngredientForm( forms.ModelForm ):

	class Meta:
		model = Ingredient
		exclude = [ 'recipe' ]
		widgets = {
				'name': forms.TextInput( attrs={ 'placeholder': 'Ingredient Name', 'class': 'span3' } ),
				'amount': forms.TextInput( attrs={ 'placeholder': 'Quantity', 'class': 'span2' } ),
				'unit': forms.Select( attrs={ 'class': 'span2' } ),
		}
