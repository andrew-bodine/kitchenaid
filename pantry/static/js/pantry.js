$( document ).ready( function( ) {
	get_pantry( );
	$( '#btn_add_pantry_item' ).click( function( ) {
		get_item( '/pantry/item/' );
	} );
} ).on( 'submit', '#form_edit_pantry_item', function( event ) {
	event.preventDefault( );
	var url = '/pantry/item/';

	var append = $( '#form_edit_pantry_item' ).attr( 'value' );
	if( append ) {
		url = url + append + '/';
	}

	$.post( 
		url,
		$( '#form_edit_pantry_item' ).serialize( ),
		function( data ) {
			$( '#edit_pantry_item_container' ).html( data );
			get_pantry( );
		}, 
		'html'
	);
} ).on( 'click', 'tr', function( ) {
	get_item( '/pantry/item/' + $( this ).attr( 'id' ) + '/' );
} ).on( 'click', '#btn_cancel_item_edit', function( ) {
	$( '#edit_pantry_item_container' ).empty( );
} ).on( 'click', '#btn_delete_item', function( ) {
	var confirmation = confirm( "Delete this item from pantry?" );
	if( confirmation == true )
		delete_item( '/pantry/item/delete/' + $( '#form_edit_pantry_item' ).attr( 'value' ) + '/' );
} );
function get_pantry( ) {
	$.ajax( {
		type: 'GET',
		url: '/pantry/contents/',
		success: function( result ) {
			$( '#pantry_contents_container' ).html( result );
		}
	} );
}
function get_item( url ) {
	$.ajax( {
		type: 'GET',
		url: url,
		success: function( result ) {
			$( '#edit_pantry_item_container' ).html( result );
		}
	} );
}
function delete_item( url ) {
	$.ajax( {
		type: 'GET',
		url: url,
		success: function( ) {
			get_pantry( );
			$( '#edit_pantry_item_container' ).empty( );
		}
	} );
}
