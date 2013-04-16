$( document ).ready( function( ) {
	get_cookbook( );
	$( '#btn_add_recipe' ).click( function( ) {
		get_recipe( '/cookbook/recipe/' );
	} );
	$( '#btn_search_recipes' ).click( function( ) {
		var data = {
			'bfilter': $( '#bsearch_filter' ).val( ),
			'sstring': $( '#bsearch_input' ).val( ),
		};
		var temp = $( '#healthy' );
		if( temp && temp.val( ) != 'Healthy?' ) {
			$.extend( data, { 'healthy': temp.val( ) } );
		}
		temp = $( '#difficulty' );
		if( temp && temp.val( ) != 'Difficulty?' ) {
			$.extend( data, { 'difficulty': temp.val( ) } );
		}
		temp = $( '#cook_time_hrs' );
		if( temp && temp.val( ) != '' ) {
			$.extend( data, { 'hrs': temp.val( ) } );
		}
		temp = $( '#cook_time_mins' );
		if( temp && temp.val( ) != '' ) {
			$.extend( data, { 'mins': temp.val( ) } );
		}
		search_cookbook( data );
	} );
	$( '#btn_advanced_search' ).click( function( ) {
		$.ajax( {
			type: 'GET',
			url: '/cookbook/advanced_search/',
			success: function( result ) {
				$( '#advanced_search_container' ).html( result );
			}
		} );
	} );
} ).on( 'click', '#btn_cancel_advanced_search', function( ) {
	$( '#advanced_search_container' ).empty( );
} ).on( 'click', '#btn_submit_recipe_form', function( ) {
	var url = '/cookbook/recipe/';

	var append = $( '#form_edit_recipe' ).attr( 'value' );
	if( append ) {
		url = url + append + '/';
	}

	$.post(
		url,
		$( '#form_edit_recipe' ).serialize( ),
		function( data ) {
			$( '#edit_recipe_container' ).html( data );
			get_cookbook( );
		},
		'html'
	);
} ).on( 'submit', '#form_edit_ingredient', function( ) {
	event.preventDefault( );
	var url = '/cookbook/ingredient/' + $( '#form_edit_recipe' ).attr( 'value' ) + '/';
	var append = $( '#form_edit_ingredient' ).attr( 'value' );
	if( append ) {
		url = url + append + '/';
	}

	$.post(
		url,
		$( '#form_edit_ingredient' ).serialize( ),
		function( data ) {
			$( '#ingredients_container' ).html( data );
		},
		'html'
	);
} ).on( 'click', '#btn_add_ingredients', function( ) {
	var url = '/cookbook/recipe/';
	var append = $( '#form_edit_recipe' ).attr( 'value' );
	if( append ) {
		url = url + append + '/';
	}

	$.post(
		url,
		$( '#form_edit_recipe' ).serialize( ),
		function( data ) {
			$( '#edit_recipe_container' ).html( data );
			append = $( '#form_edit_recipe' ).attr( 'value' );
			if( append ) {
				get_ingredients( '/cookbook/ingredient/' + append + '/' );
			}
		},
		'html'
	);
} ).on( 'click', '#cookbook_contents_container tr', function( ) {
	get_recipe( '/cookbook/recipe/' + $( this ).attr( 'id' ) + '/' );
} ).on( 'click', '#btn_cancel_recipe_edit', function( ) {
	$( '#edit_recipe_container' ).empty( );
} );
function get_recipe( url ) {
	$.ajax( {
		type: 'GET',
		url: url,
		success: function( result ) {
			$( '#edit_recipe_container' ).html( result );
			append = $( '#form_edit_recipe' ).attr( 'value' );
			if( append ) {
				get_ingredients( '/cookbook/ingredient/' + append + '/' );
			}
		}
	} );
}
function get_cookbook( ) {
	$.ajax( {
		type: 'GET',
		url: '/cookbook/contents/',
		success: function( result ) {
			$( '#cookbook_contents_container' ).html( result );
		}
	} );
}
function get_ingredients( url ) {
	$.ajax( {
		type: 'GET',
		url: url,
		success: function( result ) {
			$( '#ingredients_container' ).html( result );
		}
	} );
}
function search_cookbook( data ) {
	$.ajax( {
		type: 'GET',
		url: '/cookbook/search/',
		data: data,
		success: function( result ) {
			$( '#cookbook_contents_container' ).html( result );
		}
	} );
}
