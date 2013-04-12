from django.conf.urls import patterns, include, url
import controllers

urlpatterns = patterns( '',
	url( r'^pantry/$', controllers.pantry ),
	url( r'^pantry/item/(?P<item_id>\d)/$', controllers.item ),
	url( r'^pantry/item/$', controllers.item ),
	url( r'^pantry/item/delete/(?P<item_id>\d)/$', controllers.item_delete ),
	url( r'^pantry/contents/$', controllers.contents ),
)
