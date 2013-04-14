from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.context_processors import csrf
from forms import *

def cookbook( request ):
	if not request.user.is_authenticated( ):
		return HttpResponseRedirect( '/' )

	return render_to_response( 'cookbook.html', { }, context_instance=RequestContext( request ) )

def recipe( request, recipe_id=None ):
	if not request.user.is_authenticated( ):
		return HttpResponseRedirect( '/' )

	if request.method == "POST":
		try:
			recipe = Recipe.objects.get( id=recipe_id )
			form = RecipeForm( request.POST, instance=recipe )
		except BaseException:
			form = RecipeForm( request.POST )

		if form.is_valid( ):
			if recipe_id is None:
				temp = form.save( commit=False )
				temp.django_user = request.user
				temp.save( )
				to_pass = csrf( request )
				to_pass.update( { 'recipe_form': RecipeForm( instance=temp ) } )
				to_pass.update( { 'recipe_id': temp.id } )
				return render_to_response( 'recipe.html', to_pass, context_instance=RequestContext( request ) )
			else:
				form.save( )
				return HttpResponse( )
		else:
			to_pass = csrf( request )
			to_pass.update( { 'recipe_form': form } )
			try:
				recipe = Recipe.objects.get( id=recipe_id )
				to_pass.update( { 'recipe_id': recipe.id } )
			except BaseException:
				pass
			return render_to_response( 'recipe.html', to_pass, context_instance=RequestContext( request ) )
	else:
		to_pass = csrf( request )
		try:
			recipe = Recipe.objects.get( id=recipe_id )
			to_pass.update( { 'recipe_form': RecipeForm( instance=recipe ) } )
			to_pass.update( { 'recipe_id': recipe_id } )
		except BaseException:
			to_pass.update( { 'recipe_form': RecipeForm( ) } )

		return render_to_response( 'recipe.html', to_pass, context_instance=RequestContext( request ) )

def ingredient( request, recipe_id, ingredient_id=None ):
	if not request.user.is_authenticated( ):
		return HttpResponseRedirect( '/' )

	if request.method == "POST":
		recipe = Recipe.objects.get( id=recipe_id )
		try:
			ingredient = Ingredient.objects.get( id=ingredient_id )
			form = IngredientForm( request.POST, instance=ingredient )
		except BaseException:
			form = IngredientForm( request.POST )

		if form.is_valid( ):
			if ingredient_id is None:
				temp = form.save( commit=False )
				temp.recipe = recipe
				temp.save( )
			else:
				form.save( )
			to_pass = csrf( request )
			to_pass.update( { 'form': IngredientForm( ) } )
			to_pass.update( { 'ingredients': recipe.ingredient_set.all( ) } )
			return render_to_response( 'ingredients.html', to_pass, context_instance=RequestContext( request ) )
		else:
			to_pass = csrf( request )
			try:
				to_pass.update( { 'form': form } )
				if not ingredient_id is None:
					to_pass.update( { 'ingredient_id': ingredient_id } )
				to_pass.update( { 'ingredients': recipe.ingredient_set.all( ) } )
			except BaseException:
				pass
			return render_to_response( 'ingredients.html', to_pass, context_instance=RequestContext( request ) )
	else:
		to_pass = csrf( request )
		try:
			ingredient = Ingredient.objects.get( id=ingredient_id )
			to_pass.update( { 'form': IngredientForm( instance=ingredient ) } )
			to_pass.update( { 'ingredient_id': ingredient_id } )
		except BaseException:
			to_pass.update( { 'form': IngredientForm( ) } )
		try:
			recipe = Recipe.objects.get( id=recipe_id )
			to_pass.update( { 'ingredients': recipe.ingredient_set.all( ) } )
		except BaseException:
			pass

		return render_to_response( 'ingredients.html', to_pass, context_instance=RequestContext( request ) )

def contents( request ):
	if not request.user.is_authenticated( ):
		return HttpResponseRedirect( '/' )

	to_pass = { 'contents': request.user.recipe_set.all( ) }
	return render_to_response( 'cookbook_contents.html', to_pass, context_instance=RequestContext( request ) )
