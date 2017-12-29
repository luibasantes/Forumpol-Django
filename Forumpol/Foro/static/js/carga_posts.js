function cargarInfo(){
	$.getJSON('/static/data/anuncios.json', function(data){
		$.each(data, function(key, val){
			/* referencia a la lista de posts */
			var lista_posts = $('.list-group');

			/* crea link hacia el post */
			var link = $("<a></a>");
			link.attr('class','post');
			link.attr('href',"{% url 'foro:hilo' %}");

			/* crea list item con info del post */
			var list = $('<li></li>');
			list.attr('class','list-group-item post-item');
			list.text(val["titulo"]);

			/* crea la info que estará en el list item */
			var fecha = $('<span></span');
			fecha.attr('class','post-info pull-right fecha');
			fecha.text(val["fecha"]);

			var user = $('<span></span>');
			user.attr('class','post-info pull-right user');
			user.text(val["op"]);

			var resp = $('<span></span>');
			resp.attr('class','post-info pull-right replies');
			var icono = $('<i></i>');
			icono.attr('class','far fa-comment icon');
			resp.text(val["respuestas"]);
			resp.prepend(icono);

			/* agregando al list item */
			list.append(fecha);
			list.append(user);
			list.append(resp);

			/* agregando al link */
			link.append(list);

			/*agregando a la lista de posts */
			lista_posts.append(link);

		})
	});
}

$(window).on('load',function() {
	cargarInfo();
});