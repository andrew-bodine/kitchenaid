from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.context_processors import csrf
from cookbook.conversions import *
from cookbook.models import *
from models import *
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
			if not item_id is None:
				to_pass.update( { 'item_id': item_id } )
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
	return render_to_response( 'pantry_contents.html', to_pass, context_instance=RequestContext( request ) )

def gen_shopping( request ):
	if not request.user.is_authenticated( ):
		return HttpResponseRedirect( '/' )
	
	recipes = [ ]
	if request.method == 'GET':
		i = 0
		while( 1 ):
			try:
				recipes.append( request.GET[ str( i ) ] )
				i+=1
			except Exception as e:
				break

		# try and get existing shopping list
		try:
			slist = request.user.shoppinglist_set.all( )[ 0 ]
		except Exception as e:
			slist = ShoppingList( )
			slist.django_user = request.user
			slist.save( )

		try:
			for r_id in recipes:
				recipe = Recipe.objects.get( id=r_id )
				for ingredient in recipe.ingredient_set.all( ):

					# query pantry for ingredient
					try:
						p_amount = PantryItem.objects.get( name=ingredient.name ).amount
					except:
						p_amount = 0

					if { 'name': ingredient.name } in slist.shoppinglistitem_set.all( ).values( 'name' ):
						slist_item = slist.shoppinglistitem_set.get( name=ingredient.name )
						try:
							if ingredient.unit == slist_item.unit:
								slist_item.amount += ingredient.amount
							else:
								slist_item.amount += function_dict[ ingredient.unit ][ slist_item.unit ]( ingredient.amount )
						except Exception as e:
							print str( e )
						slist_item.save( )
					
					elif not p_amount > ingredient.amount:
							item = ShoppingListItem( )
							item.name = ingredient.name
							item.amount = ingredient.amount - p_amount
							item.unit = ingredient.unit
							item.list = slist
							item.save( )
		except Exception as e:
			print str( e )

		return HttpResponse( )

def commit_shopping( request ):
	if not request.user.is_authenticated( ):
		return HttpResponseRedirect( '/' )
	
	to_pass = csrf( request )

	if request.method == 'POST':
		pass
	else:
		try:
			instance = request.user.shoppinglist_set.all( )[ 0 ]
			to_pass.update( { 'items': instance.shoppinglistitem_set.all( ) } )
			print to_pass
		except Exception as e:
			print str( e )
			to_pass.update( { 'items': [ ] } )
		to_pass.update( { 'units': units } )
		return render_to_response( 'edit_shopping.html' , to_pass )

def shopping( request ):
	if not request.user.is_authenticated( ):
		return HttpResponseRedirect( '/' )

	try:
		to_pass = { 'list': request.user.shoppinglist_set.all( )[ 0 ].shoppinglistitem_set.all( ) }
	except:
		to_pass = { 'list': [ ] }
	return render_to_response( 'shopping.html', to_pass )
