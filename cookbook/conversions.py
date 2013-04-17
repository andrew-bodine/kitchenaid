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
