var num_posts

window.onload = function(){
	/* Cuenta cuantos posts hay en la página */
	num_posts = $('.rep').length;
}
$(".año-btn").on("click", function(event) {
    $("#año-form").show();
});

$(".resp-btn").on("click", function(event) {
	$("#resp-box").show();
});

$(".editar-btn").on("click", function(event) {
	$(".editar").show();
});

