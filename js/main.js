
(function ($) {

    $( "#slider" ).slider({
			value: 1,
			min: 1,
			max: 8,
			step: 1,
        width: '100px',
			slide: function( event, ui ) {
			    $( "#amount" ).html("Studying for "+ui.value+" years");
                            update(ui.value);
			}
		});
    update(1);
    update(1);

})(jQuery);
