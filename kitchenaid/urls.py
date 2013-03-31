from django.conf.urls import patterns, include, url
from django.contrib import admin
import controllers

admin.autodiscover( )

urlpatterns = patterns( '',
	url( r'^$', controllers.gate_keeper ),
	url( r'^login/$', controllers.login_foodie ),
	url( r'^logout/$', controllers.logout_foodie ),
    	url( r'^admin/', include( admin.site.urls ) ),

	# Uncomment the admin/doc line below to enable admin documentation:
    	# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
