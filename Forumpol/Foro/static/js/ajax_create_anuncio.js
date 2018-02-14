$(document).ready(function(){
	$("#create-form").submit(function(e){
		e.preventDefault();
		var formData = new FormData($(this)[0]);
		$.ajax({
			url: window.location.origin + "/api/posts/",
			type: $(this).attr('method'),
			data: formData,
			cache: false,
    		contentType: false,
    		processData: false,
			success: function(json){
					$tooltip= $('<div class="alert alert-success alert-dismissable"> <button type="button" class="close" data-dismiss="alert">&times;</button>Su post ha sido enviado con éxito, espere a que algún moderador lo apruebe para visualizarlo.</div>');
					$("#categoria").append($tooltip)
			},
			error: function(e){
				$tooltip= $('<div class="alert alert-danger alert-dismissable"> <button type="button" class="close" data-dismiss="alert">&times;</button>Hubo un error al procesar su post o el formato de archivo no es correcto. <strong> Sólo debe enviar archivos de imágenes (.jpg, .png, .gif) </strong></div>');
				$("#categoria").append($tooltip)
			}
		});
	});
});

