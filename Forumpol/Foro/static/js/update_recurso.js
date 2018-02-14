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
	$("#update-form").submit(function(e){
		e.preventDefault();
		var url= ""+window.location
		var url_list=url.split("/")
		var id= url_list[url_list.length - 2]
		var csrftoken = readCookie('csrftoken');
		$.ajaxSetup({

        beforeSend: function(xhr) {
        	xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    	});
    	var tag=$("#tags").val().split(",")
		var data= {'titulo':$("#titulo").val(),'autor':$("#autor").val(),'descripcion':$("#descripcion").val(),'tags':tag}
    	var json= JSON.stringify(data); 
		$.ajax({
			headers: { 
        		'Accept': 'application/json',
        		'Content-Type': 'application/json' 
    		},
			url: window.location.origin + "/api/recursos/edit/" + id + "/",
			type: $(this).attr('method'),
			data: json,
			cache: false,
    		contentType: false,
    		processData: false,
			success: function(json){
					$tooltip= $('<div class="alert alert-success alert-dismissable"> <button type="button" class="close" data-dismiss="alert">&times;</button>Su post ha sido enviado con éxito, espere a que algún moderador lo apruebe para visualizarlo.</div>');
					$("#repo_body").append($tooltip)
			},
			error: function(e){
				$tooltip= $('<div class="alert alert-danger alert-dismissable"> <button type="button" class="close" data-dismiss="alert">&times;</button>Hubo un error al procesar su peticion</div>');
				$("#repo_body").append($tooltip)
			}
		});
	});
});
