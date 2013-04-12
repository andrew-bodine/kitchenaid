from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.context_processors import csrf
from forms import *

def pantry( request ):
	if not request.user.is_authenticated( ):
		return HttpResponseRedirect( '/' )

	return render_to_response( 'pantry.html', { }, context_instance=RequestContext( request ) )

def item( request, item_id=None ):
	if not request.user.is_authenticated( ):
		return HttpResponseRedirect( '/' )

	if request.method == "POST":
		if item_id is None:
			form = PantryItemForm( request.POST )
		else:
			try:
				item = PantryItem.objects.get( id=item_id )
				form = PantryItemForm( request.POST, instance=item )
			except BaseException:
				form = PantryItemForm( request.POST )

		if form.is_valid( ):
			if item_id is None:
				temp = form.save( commit=False )
				temp.django_user = request.user
				temp.save( )
			else:
				form.save( )
			return HttpResponse( )
		else:
			to_pass = csrf( request )
			to_pass.update( { 'form': form } )
			return render_to_response( 'item.html', to_pass, context_instance=RequestContext( request ) )
	else:
		to_pass = csrf( request )

		if item_id is None:
			to_pass.update( { 'form': PantryItemForm( ) } )
			
		else:
			try:
				item = PantryItem.objects.get( id=item_id )
				to_pass.update( { 'form': PantryItemForm( instance=item ) } )
				to_pass.update( { 'item_id': item_id } )
			except BaseException:
				to_pass.update( { 'form': PantryItemForm( ) } )

		return render_to_response( 'item.html', to_pass, context_instance=RequestContext( request ) )

def item_delete( request, item_id ):
	if not request.user.is_authenticated( ):
		return HttpResponseRedirect( '/' )

	try:
		item = PantryItem.objects.get( id=item_id )
		item.delete( )
	except BaseException:
		pass

	return HttpResponse( )

def contents( request ):
	if not request.user.is_authenticated( ):
		return HttpResponseRedirect( '/' )

	to_pass = { 'contents': request.user.pantryitem_set.all( ) }
	return render_to_response( 'contents.html', to_pass, context_instance=RequestContext( request ) )
