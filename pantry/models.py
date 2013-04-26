from django.contrib.auth.models import User
from django.db import models

# choices
units = (
	( '', 'Units' ),
	( 'tsp', 'teaspoon' ),
	( 'tbsp', 'tablespoon' ),
	( 'c', 'cup' ),
	( 'fl oz', 'fluid ounce' ),
	( 'pt', 'pint' ),
	( 'qt', 'quart' ),
	( 'gal', 'gallon' ),
	( 'oz', 'ounce' ),
	( 'lb', 'pound' ),
	( 'whole', 'whole item' ),
)

class PantryItem( models.Model ):

	# metadatas
	name = models.CharField( max_length=50 )
	amount = models.DecimalField( max_digits=7, decimal_places=4 )
	unit = models.CharField( max_length=5, choices=units, default='', blank=False )

	# relations
	django_user = models.ForeignKey( User )

	# methods
	def __unicode__( self ):
		return self.name

class ShoppingList( models.Model ):

	# relations
	django_user = models.ForeignKey( User )

	# methods
	def __unicode__( self ):
		return str( self.id )


class ShoppingListItem( models.Model ):

	# metadatas
	name = models.CharField( max_length=50 )
	amount = models.DecimalField( max_digits=7, decimal_places=4 )
	unit = models.CharField( max_length=5, choices=units, default='', blank=False )

	# relations
	list = models.ForeignKey( ShoppingList )

	# methods
	def __unicode__( self ):
		return self.name
