$(document).ready(function() {
	var repo_url= window.location.origin + "/foro/repositorio/"
	var split = window.location.href.split("/")
	var user = split[split.length - 2]
	$.ajax({
			url: window.location.origin + "/api/recursos/" + user + "/",
			type: "GET",
			success: function(json){
				$table= $('#myTable>tbody');
				json.forEach(function(data){
					if(data.is_active==true && data.categoria=="archivo"){
						var $row= $('<tr></tr>')
						var fecha= new Date(data.fecha_creacion)
						var stringFecha=fecha.getUTCDate() +"/" + (fecha.getUTCMonth()+1) + "/" + fecha.getUTCFullYear() + "-" + (fecha.getUTCHours()) + ":" + (fecha.getUTCMinutes() + 1) + ":" + (fecha.getUTCSeconds() + 1);
						var $date= $('<td>'+stringFecha+'</td>')
						//$a_content.attr("href", json["posts_url"]+data.id);
						var $titulo= $('<td></td>')
						var $a_link= $("<a href=''>"+data.titulo+'</a>')
						$a_link.attr("href",repo_url+data.id)
						$titulo.append($a_link)
						$row.append($titulo);
						$row.append($date);
						$table.append($row);
					}
				});

			    $('#myTable').DataTable( {
			        "language": {
			            "lengthMenu": "Mostrando _MENU_ registros por pagina",
			            "zeroRecords": "No pudimos encontrar registros. Lo sentimos",
			            "info": "Mostrando pagina  _PAGE_ de _PAGES_",
			            "infoEmpty": "No hay registros",
			            "infoFiltered": "(filtrado desde _MAX_ el total de registros)",
			            "paginate": {
			                "first":      "Primero",
			                "last":       "Ultimo",
			                "next":       "Siguiente",
			                "previous":   "Anterior"
			            }
			        }
			    } );

			}
	});
} );