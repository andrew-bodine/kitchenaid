from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from forms import *

def gate_keeper( request ):

	if request.user.is_authenticated( ):
		return render_to_response( 'pantry.html', { }, context_instance=RequestContext( request ) )
	else:
		if request.method == 'GET':
			to_pass = csrf( request )
			login_form = FoodieCredentialsForm( )
			registration_form = FoodieRegistrationForm( )
			to_pass.update( { 'login_form': login_form, 'registration_form': registration_form } )
			return render_to_response( 'login_or_register.html', to_pass, context_instance=RequestContext( request ) )

def register_foodie( request ):
	if not request.user.is_authenticated( ):
		if request.method == 'POST':
			registration_form = FoodieRegistrationForm( request.POST )

			if registration_form.is_valid( ):
				if request.POST[ 'password' ] == request.POST[ 'password_again' ]:
					###############
					pass
				else:
					to_pass = csrf( request )
					registration_form.errors.update( { 'password': 'passwords do not match' } )
					to_pass.update( { 'registration_form': registration_form } )
					to_pass.update( { 'login_form': FoodieCredentialsForm( ) } )
					return render_to_response( 'login_or_register.html', to_pass, context_instance=RequestContext( request ) )
			else:
				to_pass = csrf( request )
				to_pass.update( { 'registration_form': registration_form } )
				to_pass.update( { 'login_form': FoodieCredentialsForm( ) } )
				return render_to_response( 'login_or_register.html', to_pass, context_instance=RequestContext( request ) )

def login_foodie( request ):
	
	if not request.user.is_authenticated( ):
		if request.method == 'POST':

			login_form = FoodieCredentialsForm( request.POST )

			if login_form.is_valid( ):
				email = login_form.cleaned_data[ 'email' ]
				password = login_form.cleaned_data[ 'password' ]
				user = authenticate( username=email, password=password )

				if user is not None:
					if user.is_active:
						login( request, user )
						try:
							return HttpResponseRedirect( request.GET[ 'next' ] )
						except BaseException:
							return HttpResponseRedirect( '/' )
					else:
						login_form.non_field_errors = 'account has been disabled'
						to_pass = csrf( request )
						registration_form = FoodieRegistrationForm( )
						to_pass.update( { 'login_form': login_form, 'registration_form': registration_form } )
						return render_to_response( 'login_or_register.html', to_pass, context_instance=RequestContext( request ) )
				else:
					login_form.non_field_errors = 'incorrect username and/or password'
					to_pass = csrf( request )
					registration_form = FoodieRegistrationForm( )
					to_pass.update( { 'login_form': login_form, 'registration_form': registration_form } )
					return render_to_response( 'login_or_register.html', to_pass, context_instance=RequestContext( request ) )
			else:
				to_pass = csrf( request )
				registration_form = FoodieRegistrationForm( )
				to_pass.update( { 'login_form': login_form, 'registration_form': registration_form } )
				return render_to_response( 'login_or_register.html', to_pass, context_instance=RequestContext( request ) )

def logout_foodie( request ):
	logout( request )
	return HttpResponseRedirect( '/' )
