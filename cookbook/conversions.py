# Common cooking mesurement conversions helper :
# rounds all calculations to 4 decimal places in correspondence
# with our assumption about quantity stores in our database

import math

# constants
rounder = 10000


# teaspoon
def tsp2tbsp( tsp ): 
	return math.ceil( ( float( tsp ) / 3 ) * rounder ) / rounder
def tsp2c( tsp ):
	return math.ceil( ( tsp2tbsp( tsp ) / 16 ) * rounder ) / rounder
def tsp2floz( tsp ):
	return math.ceil( ( tsp2c( tsp ) * 8 ) * rounder ) / rounder
def tsp2pt( tsp ):
	return math.ceil( ( tsp2c( tsp ) / 2 ) * rounder ) / rounder
def tsp2qt( tsp ):
	return math.ceil( ( tsp2pt( tsp ) / 2 ) * rounder ) / rounder
def tsp2gal( tsp ):
	return math.ceil( ( tsp2qt( tsp ) / 4 ) * rounder ) / rounder
def tsp2oz( tsp ):
	return math.ceil( ( tsp2floz( tsp ) ) * rounder ) / rounder
def tsp2lb( tsp ):
	return math.ceil( ( tsp2oz( tsp ) / 16 ) * rounder ) / rounder

# tablespoon
def tbsp2tsp( tbsp ):
	return math.ceil( ( float( tbsp ) * 3 ) * rounder ) / rounder
def tbsp2c( tbsp ):
	return tsp2c( tbsp2tsp( tbsp ) )
def tbsp2floz( tbsp ):
	return tsp2floz( tbsp2tsp( tbsp ) )
def tbsp2pt( tbsp ):
	return tsp2pt( tbsp2tsp( tbsp ) )
def tbsp2qt( tbsp ):
	return tsp2qt( tbsp2tsp( tbsp ) )
def tbsp2gal( tbsp ):
	return tsp2gal( tbsp2tsp( tbsp ) )
def tbsp2oz( tbsp ):
	return tsp2oz( tbsp2tsp( tbsp ) )
def tbsp2lb( tbsp ):
	return tbsp2lb( tbsp2tsp( tbsp ) )

# cup
def c2tsp( cup ):
	return math.ceil( ( float( cup ) * 16 ) * rounder ) / rounder
def c2tbsp( cup ):
	return tsp2tbsp( c2tsp( cup ) )
def c2floz( cup ):
	return tsp2floz( c2tsp( cup ) )
def c2pt( cup ):
	return tsp2pt( c2tsp( cup ) )
def c2qt( cup ):
	return tsp2qt( c2tsp( cup ) )
def c2gal( cup ):
	return tsp2gal( c2tsp( cup ) )
def c2oz( cup ):
	return tsp2oz( c2tsp( cup ) )
def c2gal( cup ):
	return tsp2gal( c2tsp( cup ) )
def c2lb( cup ):
	return tsp2lb( c2tsp( cup ) )

# fluid ounce
def floz2tsp( floz ):
	return c2tsp( float( floz ) / 8 )
def floz2tbsp( floz ):
	return tsp2tbsp( floz2tsp( floz ) )
def floz2c( floz ):
	return tsp2c( floz2tsp( floz ) )
def floz2pt( floz ):
	return tsp2pt( floz2tsp( floz ) )
def floz2qt( floz ):
	return tsp2qt( floz2tsp( floz ) )
def floz2gal( floz ):
	return tsp2gal( floz2tsp( floz ) )
def floz2oz( floz ):
	return tsp2oz( floz2tsp( floz ) )
def floz2lb( floz ):
	return tsp2lb( floz2tsp( floz ) )
	
# pint
def pt2tsp( pint ):
	return c2tsp( float( pint ) * 2 )
def pt2tbsp( pint ):
	return tsp2tbsp( pt2tsp( pint ) )
def pt2c( pint ):
	return tsp2cp( pt2tsp( pint ) )
def pt2floz( pint ):
	return tsp2floz( pt2tsp( pint ) )
def pt2qt( pint ):
	return tsp2qt( pt2tsp( pint ) )
def pt2gal( pint ):
	return tsp2gal( pt2tsp( pint ) )
def pt2oz( pint ):
	return tsp2oz( pt2tsp( pint ) )
def pt2lb( pint ):
	return tsp2lb( pt2tsp( pint ) )

# quart
def qt2tsp( quart ):
	return c2tsp( float( quart ) * 4 )
def qt2tbsp( quart ):
	return tsp2tbsp( qt2tsp( quart ) )
def qt2c( quart ):
	return tsp2c( qt2tsp( quart ) )
def qt2floz( quart ):
	return tsp2floz( qt2tsp( quart ) )
def qt2pt( quart ):
	return tsp2pt( qt2tsp( quart ) )
def qt2gal( quart ):
	return tsp2gal( qt2tsp( quart ) )
def qt2oz( quart ):
	return tsp2oz( qt2tsp( quart ) )
def qt2lb( quart ):
	return tsp2lb( qt2tsp( quart ) )

# gal
def gal2tsp( gal ):
	return gal2tsp( float( gal ) * 16 )
def gal2tbsp( gal ):
	return tsp2tbsp( gal2tsp( gal ) )
def gal2c( gal ):
	return tsp2c( gal2tsp( gal ) )
def gal2floz( gal ):
	return tsp2floz( gal2tsp( gal ) )
def gal2pt( gal ):
	return tsp2pt( gal2tsp( gal ) )
def gal2qt( gal ):
	return tsp2qt( gal2tsp( gal ) )
def gal2oz( gal ):
	return tsp2oz( gal2tsp( gal ) )
def gal2lb( gal ):
	return tsp2lb( gal2tsp( gal ) )

# oz
def oz2tsp( oz ):
	return float( oz ) * 6
def oz2tbsp( oz ):
	return tsp2tbsp( oz2tsp( oz ) )
def oz2c( oz ):
	return tsp2c( oz2tsp( oz ) )
def oz2floz( oz ):
	return tsp2floz( oz2tsp( oz ) )
def oz2pt( oz ):
	return tsp2pt( oz2tsp( oz ) )
def oz2qt( oz ):
	return tsp2qt( oz2tsp( oz ) )
def oz2gal( oz ):
	return tsp2gal( oz2tsp( oz ) )
def oz2lb( oz ):
	return tsp2lb( oz2tsp( oz ) )

# lb
def lb2tsp( lb ):
	return oz2tsp( float( lb ) * 16 )
def lb2tbsp( lb ):
	return tsp2tbsp( lb2tsp( lb ) )
def lb2c( lb ):
	return tsp2c( lb2tsp( lb ) )
def lb2floz( lb ):
	return tsp2floz( lb2tsp( lb ) )
def lb2pt( lb ):
	return tsp2pt( lb2tsp( lb ) )
def lb2qt( lb ):
	return tsp2qt( lb2tsp( lb ) )
def lb2gal( lb ):
	return tsp2gal( lb2tsp( lb ) )
def lb2oz( lb ):
	return tsp2oz( lb2tsp( lb ) )

# function dictionary
function_dict = {
	'tsp': {
		'tbsp': tsp2tbsp,
		'c': tsp2c,
		'fl oz': tsp2floz,
		'pt': tsp2pt,
		'qt': tsp2qt,
		'gal': tsp2gal,
		'oz': tsp2oz,
		'lb': tsp2lb,
	},
	'tbsp': {
		'tsp': tbsp2tsp,
		'c': tbsp2c,
		'fl oz': tbsp2floz,
		'pt': tbsp2pt,
		'qt': tbsp2qt,
		'gal': tbsp2gal,
		'oz': tbsp2oz,
		'lb': tbsp2lb,
	},
	'c': {
		'tsp': c2tsp,
		'tbsp': c2tbsp,
		'fl oz': c2floz,
		'pt': c2pt,
		'qt': c2qt,
		'gal': c2gal,
		'oz': c2oz,
		'lb': c2lb,
	},
	'fl oz': {
		'tsp': floz2tsp,
		'tbsp': floz2tbsp,
		'c': floz2c,
		'pt': floz2pt,
		'qt': floz2qt,
		'gal': floz2gal,
		'oz': floz2oz,
		'lb': floz2lb,
	},
	'pt': {
		'tsp': pt2tsp,
		'tbsp': pt2tbsp,
		'c': pt2c,
		'fl oz': pt2floz,
		'qt': pt2qt,
		'gal': pt2gal,
		'oz': pt2oz,
		'lb': pt2lb,
	},
	'qt': {
		'tsp': qt2tsp,
		'tbsp': qt2tbsp,
		'c': qt2c,
		'fl oz': qt2floz,
		'qt': qt2pt,
		'gal': qt2gal,
		'oz': qt2oz,
		'lb': qt2lb,
	},
	'gal': {
		'tsp': gal2tsp,
		'tbsp': gal2tbsp,
		'c': gal2c,
		'fl oz': gal2floz,
		'qt': gal2pt,
		'gal': gal2qt,
		'oz': gal2oz,
		'lb': gal2lb,
	},
	'oz': {
		'tsp': oz2tsp,
		'tbsp': oz2tbsp,
		'c': oz2c,
		'fl oz': oz2floz,
		'qt': oz2pt,
		'gal': oz2qt,
		'oz': oz2gal,
		'lb': oz2lb,
	},
	'lb': {
		'tsp': lb2tsp,
		'tbsp': lb2tbsp,
		'c': lb2c,
		'fl oz': lb2floz,
		'qt': lb2pt,
		'gal': lb2qt,
		'oz': lb2gal,
		'lb': lb2oz,
	},
}
