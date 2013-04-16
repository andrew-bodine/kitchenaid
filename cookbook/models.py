from django.db import models
from pantry.models import units
from django.contrib.auth.models import User

# choices
difficulties = (
	( '', 'Difficulty' ),
	( 'Easy', 'Easy' ),
	( 'Medium', 'Medium' ),
	( 'Hard', 'Hard' ),
)
meals = (
	( '', 'Meal Time' ),
	( 'Breakfast', 'Breakfast' ),
	( 'Lunch', 'Lunch' ),
	( 'Dinner', 'Dinner' ),
	( 'Snack', 'Snack' ),
)

class Recipe( models.Model ):

	# metadatas
	name = models.CharField( max_length=256 )
	preparation_hours = models.IntegerField( max_length=2 )
	preparation_minutes = models.IntegerField( max_length=2 )
	difficulty = models.CharField( max_length=6, choices=difficulties, default='', blank=False )
	is_healthy = models.BooleanField( )
	meal_time = models.CharField( max_length=9, choices=meals, default='', blank=False )
	directions = models.TextField( blank=True )

	# relations
	django_user = models.ForeignKey( User )

	# methods
	def __unicode__( self ):
		return self.name

class Ingredient( models.Model ):

	# metadatas
	name = models.CharField( max_length=50 )
	amount = models.DecimalField( max_digits=7, decimal_places=4 )
	unit = models.CharField( max_length=5, choices=units, default='', blank=False )

	# relations
	recipe = models.ForeignKey( Recipe )

	# methods
	def __unicode__( self ):
		return self.name
