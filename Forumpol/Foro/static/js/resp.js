var num_posts

window.onload = function(){
	/* Cuenta cuantos posts hay en la página */
	num_posts = $('.rep').length;
}

$(".resp-btn").on("click", function(event) {
	$("#resp-box").show();
});

$(".editar-btn").on("click", function(event) {
	$(".editar").show();
});

