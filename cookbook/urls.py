from django.conf.urls import patterns, include, url
import controllers

urlpatterns = patterns( '',
	url( r'^cookbook/$', controllers.cookbook ),
	url( r'^cookbook/ingredient/(?P<recipe_id>\d)/(?P<ingredient_id>\d)/$', controllers.ingredient ),
	url( r'^cookbook/ingredient/(?P<recipe_id>\d)/$', controllers.ingredient ),
	url( r'^cookbook/recipe/(?P<recipe_id>\d)/$', controllers.recipe ),
	url( r'^cookbook/recipe/$', controllers.recipe ),
	url( r'^cookbook/contents/$', controllers.contents ),
	url( r'^cookbook/search/$', controllers.search ),
	url( r'^cookbook/advanced_search/$', controllers.advanced ),
	url( r'^cookbook/fio_forme/', controllers.fio_forme ),
)
