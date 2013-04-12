from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.context_processors import csrf
from forms import *

def pantry( request ):
	return render_to_response( 'pantry.html', { }, context_instance=RequestContext( request ) )

def item( request ):
	if request.method == "POST":
		form = PantryItemForm( request.POST )
		if form.is_valid( ):
			temp = form.save( commit=False )
			temp.django_user = request.user
			temp.save( )
			return HttpResponse( )
		else:
			to_pass = csrf( request )
			to_pass.update( { 'form': form } )
			return render_to_response( 'item.html', to_pass, context_instance=RequestContext( request ) )
	else:
		to_pass = csrf( request )
		to_pass.update( { 'form': PantryItemForm( ) } )
		return render_to_response( 'item.html', to_pass, context_instance=RequestContext( request ) )

def contents( request ):
	to_pass = { 'contents': request.user.pantryitem_set.all( ) }
	return render_to_response( 'contents.html', to_pass, context_instance=RequestContext( request ) )
