$( document ).ready( function( ) {
	update_contents( );
	$( "#btn_add_pantry_item" ).click( function( ) {
		$.ajax( {
			type: "GET",
			url: "/pantry/item/",
			success: function( result ) {
				$( "#edit_pantry_item_container" ).html( result );
			}
		} );
	} );
} ).on( 'submit', "#form_edit_pantry_item", function( event ) {
	event.preventDefault( );
	$.post( 
		'/pantry/item/',
		$( "#form_edit_pantry_item" ).serialize( ),
		function( data ) {
			$( "#edit_pantry_item_container" ).html( data );
			update_contents( );
		}, 
		"html" 
	);
} );
function update_contents( ) {
	$.ajax( {
		type: "GET",
		url: "/pantry/contents/",
		success: function( result ) {
			$( "#pantry_contents_container" ).html( result );
		}
	} );
}
