from django.contrib.auth.models import User
from django.db import models

# choices
units = (
	( 'tbsp', 'tablespoon' ),
	( 'tsp', 'teaspoon' ),
	( 'c', 'cup' ),
	( 'fl oz', 'fluid ounces' ),
	( 'pt', 'pint' ),
	( 'qt', 'quart' ),
	( 'gal', 'gallon' ),
	( 'oz', 'ounces' ),
	( 'lb', 'pound' ),
	( 'ml', 'milimeter' ),
	( 'cc', 'cubic centimeters' ),
	( 'in', 'inch' ),
	( 'cm', 'centimeters' ),
	( 'whole', 'whole item' ),
)

class PantryItem( models.Model ):

	# metadatas
	name = models.CharField( max_length=50, unique=True )
	amount = models.DecimalField( max_digits=7, decimal_places=4 )
	unit = models.CharField( max_length=5, choices=units )

	# relations
	django_user = models.ForeignKey( User )

	# methods
	def __unicode__( self ):
		return self.name
