function readCookie(name) {
            var nameEQ = name + "=";
            var ca = document.cookie.split(';');
            for (var i = 0; i < ca.length; i++) {
                var c = ca[i];
                while (c.charAt(0) == ' ') c = c.substring(1, c.length);
                if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
            }
            return null;
}


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
					var id= json.id
					var category= "anuncio"
					var topic= $("#id_topic")[0].value
					var datos= {"category":category,"topic":topic,"op":id}
					var body= JSON.stringify(datos);
					var csrftoken = readCookie('csrftoken');
            		$.ajaxSetup({

                    beforeSend: function(xhr) {
                    	xhr.setRequestHeader("X-CSRFToken", csrftoken);
                    }
                	});
					$.ajax({
						    headers: {
                        		'Accept': 'application/json',
                        		'Content-Type': 'application/json'
                    		},
                			url: window.location.origin + "/api/threads/anuncios/",
                			type: "POST",
                			data: body,
                			cache: false,
                    		contentType: false,
                    		processData: false,
                    		success: function(json){
                    		    $tooltip= $('<div class="alert alert-success alert-dismissable"> <button type="button" class="close" data-dismiss="alert">&times;</button>Su post ha sido enviado con éxito, espere a que algún moderador lo apruebe para visualizarlo.</div>');
					            $("#categoria").append($tooltip)
                    		},
                    		error: function(e){
                    		    console.log(e)
                    		    $tooltip= $('<div class="alert alert-danger alert-dismissable"> <button type="button" class="close" data-dismiss="alert">&times;</button>Hubo un error al procesar su post o el formato de archivo no es correcto. <strong> Sólo debe enviar archivos de imágenes (.jpg, .png, .gif) </strong></div>');
				                $("#categoria").append($tooltip)
                    		}
                    });
			},
			error: function(e){
			    console.log(e)
				$tooltip= $('<div class="alert alert-danger alert-dismissable"> <button type="button" class="close" data-dismiss="alert">&times;</button>Hubo un error al procesar su post o el formato de archivo no es correcto. <strong> Sólo debe enviar archivos de imágenes (.jpg, .png, .gif) </strong></div>');
				$("#categoria").append($tooltip)
			}
		});
	});
});

