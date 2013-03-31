from django.db import models
from django.contrib.auth.models import User

class Foodie( models.Model ):

	# metadatas

	# relations
	django_user = models.OneToOneField( User, related_name='profile' )

	# methods
	def __unicode__( self ):
		return self.django_user.username
